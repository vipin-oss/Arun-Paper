#!/usr/bin/env python3
"""
P1-03 extended validation for repeated-root k-Galois hull enumeration.

Two independent layers are checked:

(A) VECTOR LEVEL (small finite fields, direct linear algebra):
    For a single component K = F_{p^d}, a compatible twist lambda, P = p^rho,
    n = P*n0, and every exponent assignment a_f in {0,...,P} for
    g = prod f^{a_f} | (x^{n0}-mu)^P, x^n-lambda, we compute
        (dim_K C, dim_K Hull_k(C))
    directly from a generator basis B of C and the code-first Gram matrix
        N_{t,r} = sum_j B_{t,j} * sigma(B_{r,j}),   sigma(v) = v^{p^k},
        dim Hull = dim C - rank(N),
    and compare with (i) the exponent formula of T4 and (ii) the transfer
    trace of T5/T6.  Dimensions here are over the component field K
    (the blueprint's F_q-dimensions are m_s times these).

(B) ORBIT-STATISTICS LEVEL (pure exact combinatorics, no field):
    For P in {2,3,4,5,8,9} and orbit lengths L = 1..6 (capped), direct
    enumeration of exponent sequences is compared with the transfer trace,
    the LCD count 2, the self-orthogonal / dual-containing closed-walk
    counts, and the exact means mu_P (L>=2) versus nu_P (L=1).

Finite checks are evidence for the tested cases only, not a proof.
No third-party packages are used.
"""
from fractions import Fraction
from itertools import product as cartesian


# ---------------------------------------------------------------- fields
class PrimeField:
    def __init__(self, p):
        self.p, self.m, self.q = p, 1, p
        self.zero, self.one = 0, 1
        self.elements = list(range(p))
        self.name = f"GF({p})"

    def add(self, a, b): return (a + b) % self.p
    def sub(self, a, b): return (a - b) % self.p
    def neg(self, a): return (-a) % self.p
    def mul(self, a, b): return (a * b) % self.p
    def pow(self, a, e):
        r = 1
        while e:
            if e & 1: r = self.mul(r, a)
            a = self.mul(a, a); e >>= 1
        return r
    def inv(self, a): return self.pow(a, self.q - 2)
    def frob(self, a, t): return self.pow(a, self.p ** t)


class GF2m:
    """GF(2^m) with elements as bit-polynomials; modulus as bit int."""

    def __init__(self, m, modulus_bits):
        self.p, self.m, self.q = 2, m, 2 ** m
        self.zero, self.one = 0, 1
        self.mod = modulus_bits
        self.elements = list(range(self.q))
        # log/exp tables with generator x (element 2)
        self.exp = [1] * (self.q - 1)
        self.log = [0] * self.q
        x = 1
        for i in range(self.q - 1):
            self.exp[i] = x
            self.log[x] = i
            x = self._mul_slow(x, 2)
        assert x == 1, "x is not primitive for this modulus"
        self.name = f"GF({self.q})"

    def _mul_slow(self, a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            b >>= 1; a <<= 1
            if a & self.q: a ^= self.mod
        return r

    def add(self, a, b): return a ^ b
    def sub(self, a, b): return a ^ b
    def neg(self, a): return a
    def mul(self, a, b):
        if a == 0 or b == 0: return 0
        return self.exp[(self.log[a] + self.log[b]) % (self.q - 1)]
    def pow(self, a, e):
        r = 1
        while e:
            if e & 1: r = self.mul(r, a)
            a = self.mul(a, a); e >>= 1
        return r
    def inv(self, a): return self.exp[(self.q - 1 - self.log[a]) % (self.q - 1)]
    def frob(self, a, t): return self.pow(a, self.p ** t)


class GF9:
    """GF(9) = F3[t]/(t^2+1); element u+3v encodes u + v*t, t^2 = -1 = 2."""

    def __init__(self):
        self.p, self.m, self.q = 3, 2, 9
        self.zero, self.one = 0, 1
        self.elements = list(range(9))
        self.name = "GF(9)"

    @staticmethod
    def _uv(a): return a % 3, a // 3

    def add(self, a, b):
        u1, v1 = self._uv(a); u2, v2 = self._uv(b)
        return ((u1 + u2) % 3) + 3 * ((v1 + v2) % 3)
    def sub(self, a, b):
        u1, v1 = self._uv(a); u2, v2 = self._uv(b)
        return ((u1 - u2) % 3) + 3 * ((v1 - v2) % 3)
    def neg(self, a):
        u, v = self._uv(a); return ((-u) % 3) + 3 * ((-v) % 3)
    def mul(self, a, b):
        u1, v1 = self._uv(a); u2, v2 = self._uv(b)
        const = (u1 * u2 + 2 * v1 * v2) % 3
        theta = (u1 * v2 + v1 * u2) % 3
        return const + 3 * theta
    def pow(self, a, e):
        r = 1
        while e:
            if e & 1: r = self.mul(r, a)
            a = self.mul(a, a); e >>= 1
        return r
    def inv(self, a): return self.pow(a, self.q - 2)
    def frob(self, a, t): return self.pow(a, self.p ** t)


# ------------------------------------------------------- polynomials over K
def trim(F, p):
    p = list(p)
    while len(p) > 1 and p[-1] == F.zero: p.pop()
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
    p = list(p); dq = len(q) - 1; inv_lc = F.inv(q[-1])
    quo = [F.zero] * max(1, len(p) - dq)
    p = list(trim(F, p))
    while len(p) - 1 >= dq and any(v != F.zero for v in p):
        d = (len(p) - 1) - dq
        c = F.mul(p[-1], inv_lc)
        if len(quo) <= d: quo.extend([F.zero] * (d - len(quo) + 1))
        quo[d] = c
        for j in range(dq + 1):
            p[d + j] = F.sub(p[d + j], F.mul(c, q[j]))
        p = list(trim(F, p))
        if len(p) - 1 < dq: break
    return trim(F, quo), trim(F, p)


def pmod(F, p, q): return pdivmod(F, p, q)[1]


def ppow(F, p, e):
    r = (F.one,)
    for _ in range(e): r = pmul(F, r, p)
    return r


def monic_polys(F, deg):
    if deg == 0:
        yield (F.one,); return
    for low in cartesian(F.elements, repeat=deg):
        yield tuple(low) + (F.one,)


def factor_distinct(F, S):
    """Distinct monic irreducible factors of a separable polynomial S."""
    factors, rem = [], S
    d = 1
    while len(rem) > 1:
        found = None
        for cand in monic_polys(F, d):
            if pmod(F, rem, cand) == (F.zero,):
                found = cand; break
        if found is None:
            d += 1; continue
        factors.append(found)
        rem = pdivmod(F, rem, found)[0]
    return factors


def rank(F, rows):
    rows = [list(r) for r in rows if any(v != F.zero for v in r)]
    if not rows: return 0
    ncol = len(rows[0]); r0 = 0; rk = 0
    for c in range(ncol):
        piv = next((i for i in range(r0, len(rows)) if rows[i][c] != F.zero), None)
        if piv is None: continue
        rows[r0], rows[piv] = rows[piv], rows[r0]
        inv = F.inv(rows[r0][c])
        rows[r0] = [F.mul(v, inv) for v in rows[r0]]
        for i in range(len(rows)):
            if i != r0 and rows[i][c] != F.zero:
                fac = rows[i][c]
                rows[i] = [F.sub(v, F.mul(fac, w)) for v, w in zip(rows[i], rows[r0])]
        r0 += 1; rk += 1
        if r0 == len(rows): break
    return rk


# ------------------------------------------------- transfer / counting (Z)
def padd(A, B):
    C = dict(A)
    for k, v in B.items(): C[k] = C.get(k, 0) + v
    return {k: v for k, v in C.items() if v}


def pmul_dict(A, B):
    C = {}
    for (k1, h1), v1 in A.items():
        for (k2, h2), v2 in B.items():
            C[(k1 + k2, h1 + h2)] = C.get((k1 + k2, h1 + h2), 0) + v1 * v2
    return C


def matmul(A, B):
    n = len(A); C = [[dict() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]: continue
            for j in range(n):
                if B[k][j]: C[i][j] = padd(C[i][j], pmul_dict(A[i][k], B[k][j]))
    return C


def matpow(A, e):
    n = len(A)
    R = [[{(0, 0): 1} if i == j else dict() for j in range(n)] for i in range(n)]
    for _ in range(e): R = matmul(R, A)
    return R


def transfer_local(L, P, w=1):
    T = [[dict() for _ in range(P + 1)] for _ in range(P + 1)]
    for a in range(P + 1):          # a = previous exponent (row)
        for b in range(P + 1):      # b = current exponent (column)
            T[a][b] = {(w * (P - b), w * min(P - b, a)): 1}
    M = matpow(T, L); out = {}
    for a in range(P + 1): out = padd(out, M[a][a])
    return out


def closed_walks(P, L, allowed):
    """tr(B^L) for 0/1 adjacency B_{a,b} = allowed(a,b), a=prev, b=current."""
    n = P + 1
    B = [[1 if allowed(a, b) else 0 for b in range(n)] for a in range(n)]
    # matrix power by repeated multiplication (small sizes only)
    def mm(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(L): R = mm(R, B)
    return sum(R[i][i] for i in range(n))


def mu_nu(P):
    mu = Fraction(P * (2 * P + 1), 6 * (P + 1))          # E[min] of two indep. uniforms
    nu = Fraction((P * P) // 4, P + 1)                  # E[min(P-A,A)], A uniform
    return mu, nu


# ------------------------------------------------------------- vector level
def sharp(F, k, f):
    d = F.m
    rho = lambda a: F.frob(a, d - k)
    r = len(f) - 1
    inv0 = F.inv(rho(f[0]))
    out = [F.zero] * (r + 1)
    for i, ci in enumerate(f):
        out[r - i] = F.mul(inv0, rho(ci))
    return trim(F, out)


def run_vector_case(F, k, lam, P, n0):
    n = P * n0
    assert 0 <= k < max(F.m, 1) or (F.m == 1 and k == 0)
    # compatibility: lambda^{1+p^{d-k}} = 1
    assert F.pow(lam, 1 + F.p ** (F.m - k)) == F.one, "incompatible twist"
    mu = next(a for a in F.elements if F.pow(a, P) == lam)
    assert F.pow(mu, 1 + F.p ** (F.m - k)) == F.one, "mu incompatible"
    # separable base S = x^{n0} - mu
    S = [F.zero] * (n0 + 1); S[0] = F.neg(mu); S[n0] = F.one
    S = trim(F, S)
    facs = factor_distinct(F, S)
    prodS = (F.one,)
    for f in facs: prodS = pmul(F, prodS, f)
    assert prodS == S, "factorization does not reconstruct S"
    # tau-orbits
    fidx = {f: i for i, f in enumerate(facs)}
    assert {sharp(F, k, f) for f in facs} == set(facs), "tau does not permute factors"
    seen, orbits = set(), []
    for f in facs:
        if f in seen: continue
        orb, cur = [], f
        while cur not in seen:
            seen.add(cur); orb.append(cur); cur = sharp(F, k, cur)
        orbits.append(orb)

    brute, formula, records = {}, {}, []
    for exps in cartesian(range(P + 1), repeat=len(facs)):
        g = (F.one,)
        for f, a in zip(facs, exps): g = pmul(F, g, ppow(F, f, a))
        degg = len(g) - 1
        dimC = n - degg
        gamma = list(g) + [F.zero] * (n - len(g))
        if dimC == 0:
            dimH = 0
        else:
            # autocorrelation Phi[delta] = sum_s gamma_s * sigma(gamma_{s+delta})
            Phi = {}
            for delta in range(-(dimC - 1), dimC):
                s_lo = max(0, -delta); s_hi = min(degg, degg - delta)
                tot = F.zero
                for s in range(s_lo, s_hi + 1):
                    tot = F.add(tot, F.mul(gamma[s], F.frob(gamma[s + delta], k)))
                Phi[delta] = tot
            N = [[Phi[t - r] for r in range(dimC)] for t in range(dimC)]
            dimH = dimC - rank(F, N)
        brute[(dimC, dimH)] = brute.get((dimC, dimH), 0) + 1
        records.append((exps, dimC, dimH))

    for exps, dimC, dimH in records:
        Hf = 0
        for orb in orbits:
            idx = [fidx[f] for f in orb]; L = len(idx)
            for i in range(L):
                ai, aprev = exps[idx[i]], exps[idx[i - 1]]
                Hf += (len(orb[i]) - 1) * min(P - ai, aprev)
        Kf = n - sum((len(f) - 1) * a for f, a in zip(facs, exps))
        assert Kf == dimC and Hf == dimH, (exps, Kf, dimC, Hf, dimH)
        formula[(Kf, Hf)] = formula.get((Kf, Hf), 0) + 1
    assert formula == brute

    transfer = {(0, 0): 1}
    for orb in orbits:
        w = len(orb[0]) - 1
        transfer = pmul_dict(transfer, transfer_local(len(orb), P, w))
    assert transfer == brute, "transfer != brute"

    total = sum(brute.values())
    muP, nuP = mu_nu(P)
    avgH = Fraction(sum(H * c for (K, H), c in brute.items()), total)
    corr = sum((len(o[0]) - 1) * (nuP if len(o) == 1 else len(o) * muP) for o in orbits)
    frozen = sum((len(o[0]) - 1) * len(o) * muP for o in orbits)
    lcd = sum(c for (K, H), c in brute.items() if H == 0)
    selforth = sum(c for (K, H), c in brute.items() if H == K)
    dualcont = sum(c for (K, H), c in brute.items() if H == n - K)
    so_pred, dc_pred = 1, 1
    for orb in orbits:
        L = len(orb)
        so_pred *= closed_walks(P, L, lambda a, b: a + b >= P)
        dc_pred *= closed_walks(P, L, lambda a, b: a + b <= P)
    print(f"\n=== VECTOR {F.name}, k={k}, lambda={lam}, mu={mu}, P={P}, n0={n0}, n={n} ===")
    print("factor degrees:", [len(f) - 1 for f in facs], " orbit lengths:", [len(o) for o in orbits])
    print(f"assignments checked: {total} (expected {(P + 1) ** len(facs)})")
    print("joint (K,H) distribution:", dict(sorted(brute.items())))
    print(f"LCD: brute {lcd} vs 2^#orbits {2 ** len(orbits)}; "
          f"self-orth: brute {selforth} vs tr(B^L) {so_pred}; "
          f"dual-cont: brute {dualcont} vs tr(B'^L) {dc_pred}")
    assert lcd == 2 ** len(orbits) and selforth == so_pred and dualcont == dc_pred
    print(f"mean Hull: brute {avgH}  corrected-split {corr}  frozen-C5 {frozen}")
    assert avgH == corr
    print("OK: Gram-rank brute force == exponent formula == transfer trace")


# ------------------------------------------------------- orbit statistics
def run_orbit_stats():
    print("\n=== ORBIT STATISTICS (exact enumeration vs transfer trace) ===")
    print("P  L  seqs        mean-brute        nu_P(L=1)   mu_P(edge)  LCD  selforth  dualcont")
    for P in (2, 3, 4, 5, 8, 9):
        muP, nuP = mu_nu(P)
        for L in range(1, 7):
            if (P + 1) ** L > 20000: continue
            direct = {}
            for seq in cartesian(range(P + 1), repeat=L):
                Kc = sum(P - a for a in seq)
                Hc = sum(min(P - seq[i], seq[i - 1]) for i in range(L))
                direct[(Kc, Hc)] = direct.get((Kc, Hc), 0) + 1
            assert direct == transfer_local(L, P, 1), (P, L)
            total = (P + 1) ** L
            meanH = Fraction(sum(H * c for (K, H), c in direct.items()), total)
            expected = nuP if L == 1 else L * muP
            assert meanH == expected, (P, L, meanH, expected)
            lcd = sum(c for (K, H), c in direct.items() if H == 0)
            so = closed_walks(P, L, lambda a, b: a + b >= P)
            dc = closed_walks(P, L, lambda a, b: a + b <= P)
            assert lcd == 2
            assert so == sum(c for (K, H), c in direct.items() if H == K)
            assert dc == sum(c for (K, H), c in direct.items() if H == L * P - K)
            print(f"{P}  {L}  {total:<10} {str(meanH):<16} {str(nuP):<10} {str(muP):<10} {lcd}    {so:<8} {dc}")
    print("OK: transfer trace == direct enumeration; L=1 mean is nu_P, L>=2 edge mean is mu_P")


if __name__ == "__main__":
    run_orbit_stats()
    run_vector_case(PrimeField(2), k=0, lam=1, P=2, n0=7)
    run_vector_case(PrimeField(3), k=0, lam=1, P=3, n0=4)
    run_vector_case(PrimeField(3), k=0, lam=2, P=3, n0=4)      # lambda = -1
    run_vector_case(GF9(), k=1, lam=1, P=3, n0=4)
    run_vector_case(GF9(), k=1, lam=2, P=3, n0=4)              # lambda = -1 (the F3 element 2 in GF(9))
    run_vector_case(GF2m(3, 0b1011), k=1, lam=1, P=2, n0=7)    # GF(8), orbit length 6
    print("\nALL P1-03 EXTENDED CHECKS PASSED")
