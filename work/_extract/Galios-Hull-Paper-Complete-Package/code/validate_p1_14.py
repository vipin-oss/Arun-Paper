#!/usr/bin/env python3
"""
P1-14 independent audit script.  NEW artifact; no earlier script is
imported or modified, and no earlier output file is touched.

Purpose: independently audit the transfer-matrix enumerator (T5/T6),
corollaries C1-C4, the corrected moment formulas (C5/C6), and three
PROPOSED new corollaries (N1 Cov(dim C, dim Hull) = 0, N2 Var(dim C),
N3 LCD refinement) -- by methods that do not reuse earlier code:

  Layer A (symbolic, needs sympy; skipped with a notice if unavailable):
      fresh symbolic re-derivation of every closed form in P1-06
      (mu_P, nu_P parity split, E[min^2], Var_edge, F(c), adjacent
      cross-moment, kappa_P, L=2 cross-moment and covariance, V_1/V_2/
      V_{L>=3} assemblies) and of gamma_self = P(P+2)/24 (for N1).
  Layer B (exact orbit combinatorics, stdlib only):
      direct enumeration of exponent tuples vs (i) fresh polynomial
      matrix-power trace, (ii) integer-evaluation matrix trace at
      several (u0, z0), (iii) explicit closed-walk enumeration (small
      cases).  Checks distribution, marginals, [z^0] = 2, C5/C6
      moments, Var(dim C) (N2), Cov(dim C, dim Hull) = 0 (N1),
      self-orthogonal / dual-containing closed-walk counts (C4),
      and the blueprint Sec.2 layer-decomposition identity.
  Layer C (fresh finite-field implementation, stdlib only):
      a from-scratch GF(p^d) (digit-encoded elements), polynomial
      factorization by trial division, tau-orbits via sharp, and
      Gram-rank brute force (dim Hull = dim C - rank of the
      code-first Gram matrix).  Compares brute force, T4 exponent
      formula, T6 transfer product, and all moment/count identities
      including N1/N2 -- plus a direct reproduction of the RR-3
      Euclidean-dual check whose original script was kept only in /tmp.
  Layer D (global assembly by exact convolution of Layer-B orbit
      distributions) for the GF(2) x GF(4) orbit multiset of P1-05,
      reproducing its published global counts (729 / 16 / 144 / 144)
     _without_ using P1-05/P1-03 code.

Finite checks are evidence for the tested cases only, not proofs.
The proofs are in P1_14_MATHEMATICAL_ADVANCEMENT.md.
"""
from fractions import Fraction
from itertools import product as cartesian

FAILS = []


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("FAIL:", msg)


# =====================================================================
# Layer A -- symbolic re-derivation (sympy; derivation aid)
# =====================================================================
def layer_A():
    print("=== LAYER A: symbolic re-derivation (sympy) ===")
    try:
        import sympy as sp
    except ImportError:
        print("sympy unavailable: Layer A SKIPPED (Layers B-D are stdlib-only)")
        return
    P, b, t, m = sp.symbols("P b t m", integer=True, positive=True)
    S = lambda e, v, lo, hi: sp.summation(e, (v, lo, hi))
    mu = P * (2 * P + 1) / (6 * (P + 1))
    eq = lambda x, y: sp.simplify(x - y) == 0

    mu_s = sp.simplify(S(((P - t + 1) / (P + 1)) ** 2, t, 1, P))
    check(eq(mu_s, mu), "A: mu_P")
    e2_s = sp.simplify(S((2 * t - 1) * ((P - t + 1) / (P + 1)) ** 2, t, 1, P))
    check(eq(e2_s, P * (P ** 2 + P + 1) / (6 * (P + 1))), "A: E[min^2]")
    vedge = P * (P + 2) * (2 * P ** 2 + 4 * P + 3) / (36 * (P + 1) ** 2)
    check(eq(e2_s - mu ** 2, vedge), "A: Var_edge")
    F = lambda cc: cc * (2 * P - cc + 1) / (2 * (P + 1))
    check(eq(sp.simplify(S((P - t + 1) / (P + 1), t, 1, sp.Symbol("c", integer=True, positive=True))), F(sp.Symbol("c", integer=True, positive=True))), "A: F(c)")
    adj = sp.simplify(S(F(P - b) * F(b), b, 0, P) / (P + 1))
    check(eq(adj, P * (P - 1) * (11 * P ** 2 + 15 * P + 6) / (120 * (P + 1) ** 2)), "A: E[Xi X(i+1)]")
    check(eq(adj - mu ** 2, -P * (P + 2) * (7 * P ** 2 + 14 * P + 9) / (360 * (P + 1) ** 2)), "A: kappa_P")
    s = sp.symbols("s", integer=True, positive=True)
    l2 = sp.simplify(S(S(((P - s - t + 1) / (P + 1)) ** 2, t, 1, P - s), s, 1, P - 1))
    check(eq(l2, P ** 2 * (P - 1) / (12 * (P + 1))), "A: E[X0 X1] (L=2)")
    check(eq(l2 - mu ** 2, -P ** 2 * (P + 2) ** 2 / (36 * (P + 1) ** 2)), "A: Cov_L2")
    check(eq(2 * (e2_s - mu ** 2) + 2 * (l2 - mu ** 2),
             P * (P + 2) * (P ** 2 + 2 * P + 3) / (18 * (P + 1) ** 2)), "A: V_2 assembly")
    check(eq((e2_s - mu ** 2) + 2 * (adj - mu ** 2),
             P * (P + 2) * (P ** 2 + 2 * P + 2) / (60 * (P + 1) ** 2)), "A: V_{L>=3} per-position assembly")
    # L = 1 parity splits as pure polynomial sums (P = 2m and P = 2m+1)
    a = sp.symbols("a", integer=True, nonnegative=True)
    nu_e = sp.simplify((S(a, a, 0, m) + S(2 * m - a, a, m + 1, 2 * m)) / (2 * m + 1))
    nu2_e = sp.simplify((S(a ** 2, a, 0, m) + S((2 * m - a) ** 2, a, m + 1, 2 * m)) / (2 * m + 1))
    check(eq(nu_e, m ** 2 / (2 * m + 1)), "A: nu_P even")
    check(eq(nu2_e, (2 * m) * ((2 * m) ** 2 + 2) / (12 * (2 * m + 1))), "A: E[X^2] L=1 even")
    check(eq(nu2_e - nu_e ** 2, (2 * m) * (2 * m + 2) * ((2 * m) ** 2 + 4 * m + 4) / (48 * (2 * m + 1) ** 2)), "A: V_1 even")
    nu_o = sp.simplify((S(a, a, 0, m) + S(2 * m + 1 - a, a, m + 1, 2 * m + 1)) / (2 * m + 2))
    nu2_o = sp.simplify((S(a ** 2, a, 0, m) + S((2 * m + 1 - a) ** 2, a, m + 1, 2 * m + 1)) / (2 * m + 2))
    check(eq(nu_o, m * (m + 1) / (2 * m + 2)), "A: nu_P odd")
    check(eq(nu2_o, (2 * m + 1) * (2 * m) / 12), "A: E[X^2] L=1 odd")
    check(eq(nu2_o - nu_o ** 2, (2 * m) * (2 * m + 4) / 48), "A: V_1 odd")
    # N1 pieces: gamma_self = Cov(B, min(B,C)) and the L=1 covariance numerator
    gself = sp.simplify(S(b * F(b), b, 0, P) / (P + 1) - (P / 2) * mu)
    check(eq(gself, P * (P + 2) / 24), "A: gamma_self = P(P+2)/24")
    cnum_e = sp.simplify((S(b ** 2, b, 0, m) + S(b * (2 * m - b), b, m + 1, 2 * m)) / (2 * m + 1))
    check(eq(cnum_e, m * nu_e), "A: L=1 Cov numerator even (= (P/2) nu_P)")
    cnum_o = sp.simplify((S(b ** 2, b, 0, m) + S(b * (2 * m + 1 - b), b, m + 1, 2 * m + 1)) / (2 * m + 2))
    check(eq(cnum_o, ((2 * m + 1) / 2) * nu_o), "A: L=1 Cov numerator odd (= (P/2) nu_P)")
    check(eq(sp.simplify(S(b ** 2, b, 0, P) / (P + 1) - (P / 2) ** 2), P * (P + 2) / 12), "A: Var(U{0..P}) (for N2)")
    print("Layer A done: every P1-06 closed form re-derived symbolically; "
          "gamma_self = P(P+2)/24 confirmed")


# =====================================================================
# Layer B -- exact orbit combinatorics (fresh implementation)
# =====================================================================
def padd(A, B):
    C = dict(A)
    for k, v in B.items():
        C[k] = C.get(k, 0) + v
    return {k: v for k, v in C.items() if v}


def pdmul(A, B):
    C = {}
    for (k1, h1), v1 in A.items():
        for (k2, h2), v2 in B.items():
            C[(k1 + k2, h1 + h2)] = C.get((k1 + k2, h1 + h2), 0) + v1 * v2
    return C


def transfer_trace_poly(P, L, w):
    """tr(T^L), T[a][b] = {(w(P-b), w*min(P-b,a)): 1}; fresh code."""
    n = P + 1
    T = [[{(w * (P - b), w * min(P - b, a)): 1} for b in range(n)] for a in range(n)]
    # matrix power by repeated multiplication
    R = [[{(0, 0): 1} if i == j else {} for j in range(n)] for i in range(n)]
    for _ in range(L):
        Rn = [[{} for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for k in range(n):
                if not R[i][k]:
                    continue
                for j in range(n):
                    if T[k][j]:
                        Rn[i][j] = padd(Rn[i][j], pdmul(R[i][k], T[k][j]))
        R = Rn
    out = {}
    for a in range(n):
        out = padd(out, R[a][a])
    return out


def orbit_enumeration(P, L, w):
    dist = {}
    for A in cartesian(range(P + 1), repeat=L):
        K = w * sum(P - A[i] for i in range(L))
        H = w * sum(min(P - A[i], A[i - 1]) for i in range(L))
        dist[(K, H)] = dist.get((K, H), 0) + 1
    return dist


def trace_int_eval(P, L, w, u0, z0):
    """tr(T^L) with integer entries substituted -- independent path."""
    n = P + 1
    T = [[(u0 ** (w * (P - b))) * (z0 ** (w * min(P - b, a))) for b in range(n)] for a in range(n)]
    def mm(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(L):
        R = mm(R, T)
    return sum(R[i][i] for i in range(n))


def closed_walk_count(P, L, allowed):
    n = P + 1
    Bm = [[1 if allowed(a, b) else 0 for b in range(n)] for a in range(n)]
    def mm(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(L):
        R = mm(R, Bm)
    return sum(R[i][i] for i in range(n))


def dist_moments(dist):
    tot = sum(dist.values())
    EK = Fraction(sum(K * c for (K, H), c in dist.items()), tot)
    EH = Fraction(sum(H * c for (K, H), c in dist.items()), tot)
    VK = Fraction(sum(K * K * c for (K, H), c in dist.items()), tot) - EK * EK
    VH = Fraction(sum(H * H * c for (K, H), c in dist.items()), tot) - EH * EH
    CKH = Fraction(sum(K * H * c for (K, H), c in dist.items()), tot) - EK * EH
    return EK, EH, VK, VH, CKH


def nu_f(P): return Fraction((P * P) // 4, P + 1)
def mu_f(P): return Fraction(P * (2 * P + 1), 6 * (P + 1))


def var_S(P, L):
    if L == 1:
        if P % 2 == 0:
            return Fraction(P * (P + 2) * (P * P + 2 * P + 4), 48 * (P + 1) ** 2)
        return Fraction((P - 1) * (P + 3), 48)
    if L == 2:
        return Fraction(P * (P + 2) * (P * P + 2 * P + 3), 18 * (P + 1) ** 2)
    return Fraction(L * P * (P + 2) * (P * P + 2 * P + 2), 60 * (P + 1) ** 2)


def layer_B():
    print("\n=== LAYER B: exact orbit combinatorics (fresh code) ===")
    # blueprint Sec.2 layer-decomposition identity, checked directly
    for P in range(1, 10):
        for ai in range(P + 1):
            for ap in range(P + 1):
                lhs = min(P - ai, ap)
                rhs = sum((1 if ap >= t else 0) * (0 if ai >= P - t + 1 else 1)
                          for t in range(1, P + 1))
                check(lhs == rhs, f"B layer-identity P={P} a_i={ai} a_prev={ap}")
    print("blueprint Sec.2 layer identity min(P-a_i, a_{i-1}) = "
          "sum_t eps_{i-1}^{(t)}(1-eps_i^{(P-t+1)}): verified for P=1..9, all pairs")

    combos = []
    for P in (1, 2, 3, 4, 5, 7, 8, 9):
        for L in range(1, 9):
            if (P + 1) ** L <= 100_000:
                combos.append((P, L))
    n_cov0 = 0
    for (P, L) in combos:
        for w in (1, 2, 3) if (P, L) in ((2, 2), (1, 3), (3, 1)) else (1,):
            enum = orbit_enumeration(P, L, w)
            tr = transfer_trace_poly(P, L, w)
            check(enum == tr, f"B trace==enum P={P} L={L} w={w}")
            # integer-evaluation path (two points)
            for (u0, z0) in ((2, 3), (3, 5)):
                val = sum(c * (u0 ** K) * (z0 ** H) for (K, H), c in enum.items())
                check(trace_int_eval(P, L, w, u0, z0) == val,
                      f"B int-eval P={P} L={L} w={w} at {(u0, z0)}")
            # total count and [z^0] (per-orbit LCD count = 2)
            check(sum(enum.values()) == (P + 1) ** L, f"B total P={P} L={L} w={w}")
            check(sum(c for (K, H), c in enum.items() if H == 0) == 2,
                  f"B [z^0]=2 P={P} L={L} w={w}")
            # z=1 code marginal per orbit: (sum_j u^{w j})^L as distribution over K
            marg = {}
            for (K, H), c in enum.items():
                marg[K] = marg.get(K, 0) + c
            pred = {0: 1}
            for _ in range(L):
                nxt = {}
                for e0, v0 in pred.items():
                    for j in range(P + 1):
                        nxt[e0 + w * j] = nxt.get(e0 + w * j, 0) + v0
                pred = nxt
            # (alpha -> P - alpha shows the two sums share one distribution)
            check(marg == pred, f"B code-marginal P={P} L={L} w={w}")
            # moments: C5 split, C6 variance, N2 Var(code), N1 Cov = 0
            EK, EH, VK, VH, CKH = dist_moments(enum)
            check(EH == (nu_f(P) if L == 1 else L * mu_f(P)) * w, f"B meanH P={P} L={L} w={w}")
            check(VH == w * w * var_S(P, L), f"B varH P={P} L={L} w={w}")
            check(VK == w * w * L * Fraction(P * (P + 2), 12), f"B varK(N2) P={P} L={L} w={w}")
            check(CKH == 0, f"B covKH(N1) P={P} L={L} w={w}: got {CKH}")
            if CKH == 0:
                n_cov0 += 1
            # C4 counts per orbit (edge conditions are termwise, so they
            # agree with the distribution counts H==K and H==w*sum alpha_i)
            so_e = sum(c for (K, H), c in enum.items() if H == K)
            dc_e = sum(c for (K, H), c in enum.items()
                       if H == w * L * P - K)
            check(so_e == closed_walk_count(P, L, lambda a, b: a + b >= P),
                  f"B selforth P={P} L={L} w={w}")
            check(dc_e == closed_walk_count(P, L, lambda a, b: a + b <= P),
                  f"B dualcont P={P} L={L} w={w}")
            check(so_e == dc_e, f"B C4 counts equal P={P} L={L} w={w}")
    print(f"orbit grid: {len(combos)} (P,L) pairs; distribution == poly-trace "
          f"== integer-evaluation trace at (2,3),(3,5); moments, C4 counts, "
          f"N1 (Cov=0 in {n_cov0} orbit configs incl. weights), N2 all checked")

    # worked example E1: P=2, L=2, w=1 -- list every tuple
    print("\nE1 worked example (P=2, L=2, w=1): all 9 exponent tuples")
    for A in cartesian(range(3), repeat=2):
        K = sum(2 - A[i] for i in range(2))
        H = sum(min(2 - A[i], A[i - 1]) for i in range(2))
        print(f"  alpha={A}: (dim C contrib, Hull contrib) = ({K}, {H})")
    # worked example E2: P=1, L=3, w=1 joint distribution
    print("E2 worked example (P=1, L=3, w=1): joint distribution =",
          dict(sorted(orbit_enumeration(1, 3, 1).items())))
    # dependence witness for N1 (uncorrelated but NOT independent)
    d = orbit_enumeration(1, 2, 1)
    tot = sum(d.values())
    pC2 = Fraction(sum(c for (K, H), c in d.items() if K == 2), tot)
    pH1 = Fraction(sum(c for (K, H), c in d.items() if H == 1), tot)
    pC2H1 = Fraction(d.get((2, 1), 0), tot)
    print(f"N1 dependence witness (P=1,L=2,w=1): Pr(C=2)={pC2}, Pr(H=1)={pH1}, "
          f"Pr(C=2,H=1)={pC2H1} != product {pC2 * pH1}  (Cov=0 yet dependent)")
    check(pC2H1 != pC2 * pH1, "B dependence witness")


# =====================================================================
# Layer C -- fresh finite fields GF(p^d), Gram-rank brute force
# =====================================================================
class GF:
    """GF(p^d): elements are ints, base-p digits = coefficients of 1,x,..."""

    def __init__(self, p, d, modulus):
        self.p, self.d, self.mod = p, d, modulus  # modulus low->high, monic, deg d
        self.q = p ** d
        self.zero, self.one = 0, 1
        self.elements = list(range(self.q))
        self.name = f"GF({self.q})"

    def _digits(self, a):
        ds = []
        for _ in range(self.d):
            ds.append(a % self.p)
            a //= self.p
        return ds

    def _from(self, ds):
        v = 0
        for c in reversed(ds[: self.d]):
            v = v * self.p + (c % self.p)
        return v

    def add(self, a, b):
        da, db = self._digits(a), self._digits(b)
        return self._from([(x + y) % self.p for x, y in zip(da, db)])

    def sub(self, a, b):
        da, db = self._digits(a), self._digits(b)
        return self._from([(x - y) % self.p for x, y in zip(da, db)])

    def neg(self, a):
        return self._from([(-x) % self.p for x in self._digits(a)])

    def mul(self, a, b):
        da, db = self._digits(a), self._digits(b)
        tmp = [0] * (2 * self.d - 1)
        for i, x in enumerate(da):
            for j, y in enumerate(db):
                tmp[i + j] = (tmp[i + j] + x * y)
        # reduce high degrees with the modulus: x^d = -(mod[0..d-1])
        for deg in range(2 * self.d - 2, self.d - 1, -1):
            c = tmp[deg] % self.p
            if c:
                for i in range(self.d):
                    tmp[deg - self.d + i] = (tmp[deg - self.d + i] - c * self.mod[i])
                tmp[deg] = 0
        return self._from([c % self.p for c in tmp[: self.d]])

    def pow(self, a, e):
        r = 1
        while e:
            if e & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            e >>= 1
        return r

    def inv(self, a):
        assert a != 0
        return self.pow(a, self.q - 2)

    def frob(self, a, t):
        return self.pow(a, self.p ** t)


def trim(F, p):
    p = list(p)
    while len(p) > 1 and p[-1] == F.zero:
        p.pop()
    return tuple(p)


def pmul(F, p, q):
    r = [F.zero] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a != F.zero:
            for j, b in enumerate(q):
                if b != F.zero:
                    r[i + j] = F.add(r[i + j], F.mul(a, b))
    return trim(F, r)


def pdivmod(F, p, q):
    p = list(trim(F, p))
    dq = len(q) - 1
    inv_lc = F.inv(q[-1])
    quo = [F.zero] * max(1, len(p) - dq)
    while len(p) - 1 >= dq and any(v != F.zero for v in p):
        dg = (len(p) - 1) - dq
        c = F.mul(p[-1], inv_lc)
        if len(quo) <= dg:
            quo.extend([F.zero] * (dg - len(quo) + 1))
        quo[dg] = c
        for j in range(dq + 1):
            p[dg + j] = F.sub(p[dg + j], F.mul(c, q[j]))
        p = list(trim(F, p))
        if len(p) - 1 < dq:
            break
    return trim(F, quo), trim(F, p)


def pmod(F, p, q):
    return pdivmod(F, p, q)[1]


def ppow(F, p, e):
    r = (F.one,)
    for _ in range(e):
        r = pmul(F, r, p)
    return r


def monic_polys(F, deg):
    if deg == 0:
        yield (F.one,)
        return
    for low in cartesian(F.elements, repeat=deg):
        yield tuple(low) + (F.one,)


def factor_distinct(F, S):
    factors, rem = [], S
    d = 1
    while len(rem) > 1:
        found = None
        for cand in monic_polys(F, d):
            if pmod(F, rem, cand) == (F.zero,):
                found = cand
                break
        if found is None:
            d += 1
            continue
        factors.append(found)
        rem = pdivmod(F, rem, found)[0]
    return factors


def rank(F, rows):
    rows = [list(r) for r in rows if any(v != F.zero for v in r)]
    if not rows:
        return 0
    ncol = len(rows[0])
    r0 = rk = 0
    for c in range(ncol):
        piv = next((i for i in range(r0, len(rows)) if rows[i][c] != F.zero), None)
        if piv is None:
            continue
        rows[r0], rows[piv] = rows[piv], rows[r0]
        iv = F.inv(rows[r0][c])
        rows[r0] = [F.mul(v, iv) for v in rows[r0]]
        for i in range(len(rows)):
            if i != r0 and rows[i][c] != F.zero:
                fac = rows[i][c]
                rows[i] = [F.sub(v, F.mul(fac, w)) for v, w in zip(rows[i], rows[r0])]
        r0 += 1
        rk += 1
        if r0 == len(rows):
            break
    return rk


def sharp(F, k, f):
    d = F.d
    rho = lambda a: F.frob(a, d - k)
    r = len(f) - 1
    inv0 = F.inv(rho(f[0]))
    out = [F.zero] * (r + 1)
    for i, ci in enumerate(f):
        out[r - i] = F.mul(inv0, rho(ci))
    return trim(F, out)


def reciprocal_plain(F, h):
    """h^sharp-plain (ordinary reciprocal, NO Frobenius) = P1-04's h^\\u2020."""
    s = len(h) - 1
    inv0 = F.inv(h[0])
    return trim(F, tuple(F.mul(inv0, h[s - i]) for i in range(s + 1)))


def run_field_case(F, k, lam, P, n0, rr3_too=False):
    n = P * n0
    d = F.d
    check(F.pow(lam, 1 + F.p ** (d - k)) == F.one, f"C compat {F.name}")
    mu = next(a for a in F.elements if F.pow(a, P) == lam)
    S = [F.zero] * (n0 + 1)
    S[0] = F.neg(mu)
    S[n0] = F.one
    S = trim(F, S)
    facs = factor_distinct(F, S)
    prod = (F.one,)
    for f in facs:
        prod = pmul(F, prod, f)
    check(prod == S, f"C factorization {F.name} lam={lam}")
    check({sharp(F, k, f) for f in facs} == set(facs), f"C tau permutes {F.name} lam={lam}")
    fidx = {f: i for i, f in enumerate(facs)}
    seen, orbits = set(), []
    for f in facs:
        if f in seen:
            continue
        orb, cur = [], f
        while cur not in seen:
            seen.add(cur)
            orb.append(cur)
            cur = sharp(F, k, cur)
        orbits.append(orb)

    brute = {}
    records = []
    for exps in cartesian(range(P + 1), repeat=len(facs)):
        g = (F.one,)
        for f, a in zip(facs, exps):
            g = pmul(F, g, ppow(F, f, a))
        degg = len(g) - 1
        dimC = n - degg
        gam = list(g) + [F.zero] * (n - len(g))
        if dimC == 0:
            dimH = 0
        else:
            Phi = {}
            for delta in range(-(dimC - 1), dimC):
                tot = F.zero
                for sidx in range(max(0, -delta), min(degg, degg - delta) + 1):
                    tot = F.add(tot, F.mul(gam[sidx], F.frob(gam[sidx + delta], k)))
                Phi[delta] = tot
            N = [[Phi[t - r] for r in range(dimC)] for t in range(dimC)]
            dimH = dimC - rank(F, N)
        brute[(dimC, dimH)] = brute.get((dimC, dimH), 0) + 1
        records.append((exps, g, dimC, dimH))

        if rr3_too:
            # RR-3 direct reproduction: shifts of h^\\u2020 are orthogonal
            # to all of C and there are deg g of them (dimension count).
            h = pdivmod(F, trim(F, tuple([F.neg(lam)] + [F.zero] * (n - 1) + [F.one])), g)[0]
            hrec = reciprocal_plain(F, h)
            shifts = []
            for i in range(n - (len(hrec) - 1)):
                row = [F.zero] * n
                for j, cj in enumerate(hrec):
                    row[i + j] = cj
                shifts.append(row)
            gen_rows = []
            for i in range(dimC):
                row = [F.zero] * n
                for j, cj in enumerate(g):
                    row[i + j] = cj
                gen_rows.append(row)
            def dot(u, v):
                acc = F.zero
                for x, y in zip(u, v):
                    acc = F.add(acc, F.mul(x, y))
                return acc

            ok_orth = all(dot(gr, sh) == F.zero
                          for gr in gen_rows for sh in shifts)
            check(ok_orth, f"C RR-3 orthogonality {F.name} exps={exps}")
            check(rank(F, shifts) == degg, f"C RR-3 dim count {F.name} exps={exps}")

    # T4 exponent formula
    formula = {}
    for exps, g, dimC, dimH in records:
        Hf = 0
        for orb in orbits:
            idx = [fidx[f] for f in orb]
            for i in range(len(idx)):
                Hf += (len(orb[i]) - 1) * min(P - exps[idx[i]], exps[idx[i - 1]])
        Kf = n - sum((len(f) - 1) * a for f, a in zip(facs, exps))
        check((Kf, Hf) == (dimC, dimH), f"C T4 {F.name} lam={lam} exps={exps}")
        formula[(Kf, Hf)] = formula.get((Kf, Hf), 0) + 1
    check(formula == brute, f"C formula==brute {F.name} lam={lam}")

    # T6 transfer product (F_q = K here, so w_O = deg f)
    transfer = {(0, 0): 1}
    for orb in orbits:
        transfer = pdmul(transfer, transfer_trace_poly(P, len(orb), len(orb[0]) - 1))
    check(transfer == brute, f"C transfer==brute {F.name} lam={lam}")

    # global statistics over the brute distribution (dims over K)
    EK, EH, VK, VH, CKH = dist_moments(brute)
    EHf = sum((len(o[0]) - 1) * (nu_f(P) if len(o) == 1 else len(o) * mu_f(P)) for o in orbits)
    VHf = sum((len(o[0]) - 1) ** 2 * var_S(P, len(o)) for o in orbits)
    VKf = sum((len(f) - 1) ** 2 for f in facs) * Fraction(P * (P + 2), 12)
    check(EH == EHf, f"C meanH {F.name} lam={lam}: {EH} vs {EHf}")
    check(VH == VHf, f"C varH {F.name} lam={lam}")
    check(VK == VKf, f"C varK N2 {F.name} lam={lam}")
    check(CKH == 0, f"C covKH N1 {F.name} lam={lam}: {CKH}")
    lcd = sum(c for (K, H), c in brute.items() if H == 0)
    check(lcd == 2 ** len(orbits), f"C LCD {F.name} lam={lam}")
    so = sum(c for (K, H), c in brute.items() if H == K)
    dc = sum(c for (K, H), c in brute.items() if H == n - K)
    sop = dcp = 1
    for o in orbits:
        sop *= closed_walk_count(P, len(o), lambda a, b: a + b >= P)
        dcp *= closed_walk_count(P, len(o), lambda a, b: a + b <= P)
    check(so == sop and dc == dcp, f"C C4 {F.name} lam={lam}")
    print(f"FIELD {F.name}, k={k}, lambda={lam}, mu={mu}, P={P}, n0={n0}, n={n}: "
          f"|F|={len(facs)}, degrees={[len(f) - 1 for f in facs]}, "
          f"orbit lengths={[len(o) for o in orbits]}, assignments={sum(brute.values())}")
    print(f"   joint (dim_K C, dim_K Hull) = {dict(sorted(brute.items()))}")
    print(f"   E[H]={EH} (formula {EHf}), Var(H)={VH}, Var(C)={VK} (N2 {VKf}), "
          f"Cov(C,H)={CKH}, LCD={lcd}=2^{len(orbits)}, selforth={so}, dualcont={dc}")
    print("   OK: Gram brute == T4 formula == T6 transfer; moments incl. N1/N2 verified")
    return brute, orbits


def layer_C():
    print("\n=== LAYER C: fresh finite-field Gram-rank brute force ===")
    GF4 = GF(2, 2, [1, 1, 1])
    GF8 = GF(2, 3, [1, 1, 0, 1])
    GF9F = GF(3, 2, [1, 0, 1])
    GF3 = GF(3, 1, [0, 1])
    run_field_case(GF4, k=1, lam=1, P=2, n0=3, rr3_too=True)
    run_field_case(GF4, k=1, lam=1, P=2, n0=5, rr3_too=True)
    run_field_case(GF9F, k=1, lam=1, P=3, n0=4)
    run_field_case(GF9F, k=1, lam=2, P=3, n0=4)
    run_field_case(GF3, k=0, lam=2, P=3, n0=4)
    run_field_case(GF8, k=1, lam=1, P=2, n0=7)


# =====================================================================
# Layer D -- global convolution for the GF(2) x GF(4) orbit multiset
# =====================================================================
def layer_D():
    print("\n=== LAYER D: global assembly, P=2, orbits (L,w) = "
          "(1,1),(2,3),(1,2),(2,6) [the P1-05 GF(2)xGF(4) example] ===")
    P, orbits = 2, [(1, 1), (2, 3), (1, 2), (2, 6)]
    glob = {(0, 0): 1}
    for (L, w) in orbits:
        glob = pdmul(glob, orbit_enumeration(P, L, w))
    tot = sum(glob.values())
    EK, EH, VK, VH, CKH = dist_moments(glob)
    EHf = sum(w * (nu_f(P) if L == 1 else L * mu_f(P)) for (L, w) in orbits)
    VHf = sum(w * w * var_S(P, L) for (L, w) in orbits)
    VKf = sum((w * w) * L for (L, w) in orbits) * Fraction(P * (P + 2), 12)
    lcd = sum(c for (K, H), c in glob.items() if H == 0)
    so = sum(c for (K, H), c in glob.items() if H == K)
    nFq = 42  # n * (m1 + m2) = 14 * 3, as in P1-05
    dc = sum(c for (K, H), c in glob.items() if H == nFq - K)
    sop = dcp = 1
    for (L, w) in orbits:
        sop *= closed_walk_count(P, L, lambda a, b: a + b >= P)
        dcp *= closed_walk_count(P, L, lambda a, b: a + b <= P)
    print(f"total={tot} (P1-05 published 729), LCD={lcd} (16), selforth={so} (144), "
          f"dualcont={dc} (144); closed-walk products {sop}/{dcp}")
    print(f"E[H]={EH} (C5-split formula {EHf}), Var(H)={VH} (C6 {VHf}), "
          f"Var(C)={VK} (N2 {VKf}), Cov(C,H)={CKH} (N1: 0)")
    check(tot == 729 and lcd == 16 and so == 144 and dc == 144, "D headline counts")
    check(so == sop and dc == dcp, "D C4 products")
    check(EH == EHf and VH == VHf and VK == VKf and CKH == 0, "D moments")
    print("OK: P1-05 global counts reproduced independently; moments verified")


if __name__ == "__main__":
    layer_A()
    layer_B()
    layer_C()
    layer_D()
    print()
    if FAILS:
        print(f"{len(FAILS)} CHECK(S) FAILED")
        raise SystemExit(1)
    print("ALL P1-14 INDEPENDENT AUDIT CHECKS PASSED")
