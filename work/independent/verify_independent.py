#!/usr/bin/env python3
"""
INDEPENDENT verification of the manuscript's hull theorems.

Deliberately written from the DEFINITIONS (Galois pairing, dual as the
orthogonal complement under that pairing, hull as a set intersection), NOT from
the paper's formulas and NOT from any script in the package.

Conventions taken from the manuscript:
  K = F_{p^d} = F_p[t]/(m), sigma(x) = x^{p^k}, rho = sigma^{-1} = x^{p^{d-k}}
  <x,y>_k = sum_i x_i sigma(y_i)            (code-first, sigma on the RIGHT)
  D(C) = C^{perp_k}, hull_k(C) = C cap D(C)
  f^#(x) = rho(c_0)^{-1} * sum_i rho(c_i) x^{r-i}   for f = sum c_i x^i
  code C_s(a) = < prod_f f^{a_f} > in K[x]/(x^n - lambda),

Everything is computed over F_p by linear algebra on packed coordinates; the
paper's exponent formulas (Theorem T4) and the transfer-matrix enumerator
(Theorem T5/T6) are then compared against that ground truth.

Exit code 0 iff all checks pass.
"""
import itertools, sys, json
from fractions import Fraction
from collections import Counter

FAILS = []


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  FAIL:", msg)
    return bool(cond)


# --------------------------------------------------------------- finite field
class GF:
    def __init__(self, p, d, poly):
        assert len(poly) == d + 1 and poly[d] == 1
        self.p, self.d, self.poly = p, d, tuple(poly)
        self.size = p ** d
        self._els = list(itertools.product(range(p), repeat=d))

    def zero(self):
        return tuple([0] * self.d)

    def one(self):
        return tuple([1] + [0] * (self.d - 1))

    def els(self):
        return self._els

    def add(self, a, b):
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def neg(self, a):
        return tuple((-x) % self.p for x in a)

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        p, d, poly = self.p, self.d, self.poly
        c = [0] * (2 * d - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        c[i + j] = (c[i + j] + x * y) % p
        for i in range(len(c) - 1, d - 1, -1):
            coef = c[i] % p
            if coef:
                for j in range(d + 1):
                    c[i - d + j] = (c[i - d + j] - coef * poly[j]) % p
        return tuple(c[i] % p for i in range(d))

    def pow_(self, a, n):
        r, b = self.one(), a
        while n:
            if n & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            n >>= 1
        return r

    def inv(self, a):
        assert a != self.zero()
        return self.pow_(a, self.size - 2)

    def from_int(self, n):
        out = []
        for _ in range(self.d):
            out.append(n % self.p)
            n //= self.p
        return tuple(out)

    def to_int(self, a):
        return sum(x * self.p ** i for i, x in enumerate(a))

    # ---- polynomials: tuples of field elements, low..high, trailing zeros trimmed,
    #      zero polynomial = () ; all divisors used here are monic.
    def trim(self, f):
        f = list(f)
        while f and f[-1] == self.zero():
            f.pop()
        return tuple(f)

    def padd(self, f, g):
        n = max(len(f), len(g))
        return self.trim(tuple(
            self.add(f[i] if i < len(f) else self.zero(),
                     g[i] if i < len(g) else self.zero()) for i in range(n)))

    def pscale(self, c, f):
        return self.trim(tuple(self.mul(c, x) for x in f))

    def pmul(self, f, g):
        if not f or not g:
            return ()
        out = [self.zero()] * (len(f) + len(g) - 1)
        for i, a in enumerate(f):
            if a == self.zero():
                continue
            for j, b in enumerate(g):
                if b != self.zero():
                    out[i + j] = self.add(out[i + j], self.mul(a, b))
        return self.trim(tuple(out))

    def pmul_all(self, fs):
        r = (self.one(),)
        for f in fs:
            r = self.pmul(r, f)
        return r

    def pmod_monic(self, f, m):
        """remainder of f modulo a monic m."""
        f = list(f)
        dg = len(m) - 1
        for i in range(len(f) - 1, dg - 1, -1):
            coef = f[i]
            if coef != self.zero():
                for j in range(dg + 1):
                    f[i - dg + j] = self.sub(f[i - dg + j], self.mul(coef, m[j]))
        while f and f[-1] == self.zero():
            f.pop()
        return tuple(f)

    def pdiv_monic(self, f, m):
        f = list(f)
        dg = len(m) - 1
        q = [self.zero()] * max(1, len(f) - dg)
        for i in range(len(f) - 1, dg - 1, -1):
            coef = f[i]
            if coef != self.zero():
                q[i - dg] = coef
                for j in range(dg + 1):
                    f[i - dg + j] = self.sub(f[i - dg + j], self.mul(coef, m[j]))
        return self.trim(tuple(q))

    def pdivides(self, m, f):
        """does the monic m divide f ?"""
        if len(f) < len(m):
            return False
        return not self.pmod_monic(f, m)

    def peval(self, f, x):
        r = self.zero()
        for c in reversed(f):
            r = self.add(self.mul(r, x), c)
        return r

    def monic(self, f):
        f = self.trim(f)
        if not f:
            return ()
        lc = f[-1]
        if lc == self.one():
            return f
        return self.pscale(self.inv(lc), f)


def is_irreducible(F, g):
    g = F.monic(g)
    deg = len(g) - 1
    if deg <= 1:
        return deg == 1
    if any(F.peval(g, a) == F.zero() for a in F.els()):
        return False
    # trial-divide by all monic polys of degree 2..deg//2
    for e in range(2, deg // 2 + 1):
        for coeffs in itertools.product(F.els(), repeat=e):
            h = tuple(list(coeffs) + [F.one()])
            if F.pdivides(h, g):
                return False
    return True


def factor_monic(F, f, maxdeg=6):
    """full factorization of a monic f into monic irreducibles (brute force)."""
    f = F.monic(f)
    out = []
    deg = len(f) - 1
    for e in range(1, maxdeg + 1):
        if 2 * e > deg + 1 and e > 1:
            break
        for coeffs in itertools.product(F.els(), repeat=e):
            h = tuple(list(coeffs) + [F.one()])
            if not is_irreducible(F, h):
                continue
            while F.pdivides(h, f):
                out.append(h)
                f = F.monic(F.pdiv_monic(f, h))
        if len(f) - 1 == 0:
            break
    if len(f) - 1 > 0:
        out.append(f)
    return out


# --------------------------------------------------------------- F_p linear algebra
def rref(rows, ncols, p):
    rows = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, len(rows)):
            if rows[i][c] % p:
                pr = i
                break
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        inv = pow(rows[r][c], -1, p)
        rows[r] = [(x * inv) % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p:
                k = rows[i][c]
                rows[i] = [(a - k * b) % p for a, b in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
        if r == len(rows):
            break
    return rows, piv


def nullspace(rows, ncols, p):
    rows, piv = rref(rows, ncols, p)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-rows[i][fc]) % p
        basis.append(v)
    return basis


def span(vectors, p):
    if not vectors:
        return []
    rows, piv = rref(vectors, len(vectors[0]), p)
    return rows[:len(piv)]


def intersect(b1, b2, n, p):
    k1, k2 = len(b1), len(b2)
    if k1 == 0 or k2 == 0:
        return []
    rows = [[0] * (k1 + k2) for _ in range(n)]
    for c in range(n):
        for i in range(k1):
            rows[c][i] = b1[i][c]
        for j in range(k2):
            rows[c][k1 + j] = (-b2[j][c]) % p
    out = []
    for s in nullspace(rows, k1 + k2, p):
        v = [0] * n
        for i in range(k1):
            if s[i]:
                for c in range(n):
                    v[c] = (v[c] + s[i] * b1[i][c]) % p
        out.append(v)
    return span(out, p)


# --------------------------------------------------------------- the paper's objects
def double(F, a, b):
    """the field element as an F_p vector, doubled (for quotient ring packing)."""
    return list(a) + list(b)


def code_basis(F, g, M, n):
    """F_p-basis of <g> in K[x]/(M), n = deg M, K = F_p^d, packed coords."""
    d = F.d
    dg = len(g) - 1
    vecs = []
    for shift in range(n - dg):
        prod = F.pmod_monic(tuple([F.zero()] * shift + list(g)), M)
        for beta in range(d):
            b = tuple(1 if i == beta else 0 for i in range(d))
            vec = []
            for i in range(n):
                c = prod[i] if i < len(prod) else F.zero()
                vec.extend(F.mul(b, c))
            vecs.append(vec)
    return span(vecs, F.p)


def dual_basis(F, cbasis, n, sigma):
    """D(C) from the DEFINITION of the pairing, by solving linear equations."""
    d, p = F.d, F.p
    rows = []
    for c in cbasis:
        # <c,y>_k = sum_j c_j sigma(y_j) is ONE field element; a vector y is in
        # the dual iff all d of its F_p coordinates vanish.  So each c gives d
        # scalar equations, the unknown being the coefficient of e_beta in y_j.
        for gam in range(d):
            row = [0] * (n * d)
            for j in range(n):
                cj = tuple(c[j * d:(j + 1) * d])
                if cj == F.zero():
                    continue
                for beta in range(d):
                    e = tuple(1 if i == beta else 0 for i in range(d))
                    val = F.mul(cj, sigma(e))          # = c_j * e_beta^sigma
                    row[j * d + beta] = val[gam] % p
            rows.append(row)
    return nullspace(rows, n * d, p)


def tau(F, f, rho):
    """f^# = rho(c_0)^{-1} sum_i rho(c_i) x^{r-i}."""
    r = len(f) - 1
    scale = F.inv(rho(f[0]))
    out = [F.zero()] * (r + 1)
    for i in range(r + 1):
        out[r - i] = F.mul(scale, rho(f[i]))
    return F.trim(tuple(out))


def run_component(p, d, polym, k, P, n0, lam_int, m_s):
    F = GF(p, d, polym)
    lam = F.from_int(lam_int)
    assert lam != F.zero(), "lambda must be a unit"
    tag = f"p={p} d={d} k={k} P={P} n0={n0} lam={F.to_int(lam)} m_s={m_s}"
    sig = lambda x: F.pow_(x, p ** k)
    rho = lambda x: F.pow_(x, p ** (d - k))

    # sigma must be an involutive-ish inverse pair as stated: rho o sigma = id
    assert all(rho(sig(x)) == x for x in F.els()), "rho != sigma^{-1}"
    compat = F.pow_(lam, 1 + p ** (d - k)) == F.one()

    mu = next((a for a in F.els() if F.pow_(a, P) == lam), None)
    assert mu is not None, "lambda has no P-th root"
    n = P * n0
    M = F.trim(tuple([F.neg(mu)] + [F.zero()] * (n - 1) + [F.one()]))
    Mbar = F.trim(tuple([F.neg(mu)] + [F.zero()] * (n0 - 1) + [F.one()]))
    assert F.pmul_all([Mbar] * P) == M, "x^n - lambda != (x^n0 - mu)^P"

    facs = factor_monic(F, Mbar, maxdeg=n0)
    assert F.pmul_all(facs) == Mbar, "factorization does not recompose Mbar"
    for f in facs:
        assert F.pdivides(f, Mbar)

    # tau permutes the irreducible factors (asserted, then checked globally)
    tau_img = {f: tau(F, f, rho) for f in facs}
    tau_ok = all(any(tau_img[f] == g for g in facs) for f in facs)
    if not tau_ok:
        return dict(tag=tag, status="N/A: tau does not preserve the factor set")

    orbits, seen = [], set()
    for f in facs:
        if f in seen:
            continue
        orb, cur = [], f
        while cur not in seen:
            seen.add(cur)
            orb.append(cur)
            cur = tau_img[cur]
        orbits.append(orb)

    weights = {f: m_s * (len(f) - 1) for f in facs}
    N = len(facs)
    if (P + 1) ** N > 60000:
        return dict(tag=tag, status=f"N/A: {(P+1)**N} assignments exceed cap")

    recs = []
    for assign in itertools.product(range(P + 1), repeat=N):
        a = dict(zip(facs, assign))
        g = F.pmul_all([f for f in facs for _ in range(a[f])])
        g = F.pmod_monic(g, M)
        dimC_lin = n - (len(g) - 1)
        cb = code_basis(F, g, M, n)
        db = dual_basis(F, cb, n, sig)
        hb = intersect(cb, db, n * d, p)
        dimC, dimD, dimH = len(cb), len(db), len(hb)
        # nondegeneracy of the Galois pairing
        assert dimC + dimD == n * d, ("dim C + dim D != n", dimC, dimD, n * d)

        # --- paper's Theorem T4 predictions
        inv_tau = {tau_img[f]: f for f in facs}
        expo = {f: max(a[f], P - a[inv_tau[f]]) for f in facs}
        dimC_T4 = sum(weights[f] * (P - a[f]) for f in facs)
        dimH_T4 = sum(weights[f] * min(P - a[f], a[inv_tau[f]]) for f in facs)
        # --- dual generator from the definition, h^# with h = Mbar/g
        h = F.pmul_all([f for f in facs for _ in range(P - a[f])])
        hsharp = tau(F, F.monic(h), rho)
        assert F.pdivides(hsharp, M), "h^# does not divide M"
        db2 = code_basis(F, F.pmod_monic(hsharp, M), M, n)
        dual_gen_ok = (span(db2, p) == span(db, p))
        lcm_expo = {f: max(a[f], sum(1 for _ in range(0))) for f in facs}
        hull_gen = F.pmul_all([f for f in facs
                               for _ in range(max(a[f], P - a[inv_tau[f]]))])
        hb2 = code_basis(F, F.pmod_monic(hull_gen, M), M, n)
        hull_gen_ok = (span(hb2, p) == span(hb, p))
        recs.append(dict(a=assign, dimC=dimC, dimD=dimD, dimH=dimH,
                         dimC_T4=dimC_T4, dimH_T4=dimH_T4,
                         hull_gen_ok=hull_gen_ok, dual_gen_ok=dual_gen_ok))

    res = dict(tag=tag, n=n, N=N, factors=[len(f) - 1 for f in facs],
               orbits=[len(o) for o in orbits], weights=[weights[f] for f in facs],
               compat=compat, count=len(recs), recs=recs)

    # ---------------- checks
    ok_dimC = all(r['dimC'] == r['dimC_T4'] for r in recs)
    ok_dimH = all(r['dimH'] == r['dimH_T4'] for r in recs)
    ok_hg = all(r['hull_gen_ok'] for r in recs)
    ok_dg = all(r['dual_gen_ok'] for r in recs)
    check(ok_dimC, f"{tag}: dim C formula (T1)")
    check(ok_dimH, f"{tag}: hull dim formula (T4)")
    check(ok_hg, f"{tag}: hull generator lcm (T4)")
    check(ok_dg, f"{tag}: dual generator h^# generates D(C) (T3/Prop transport)")

    # enumerator: brute force vs product of transfer-matrix traces
    cnt = Counter((r['dimC'], r['dimH']) for r in recs)
    pred = Counter({(0, 0): 1})
    for orb in orbits:
        w = weights[orb[0]]
        t = transfer_trace(P, w, len(orb))
        newp = Counter()
        for (K0, H0), c0 in pred.items():
            for (du, dz), c1 in t.items():
                newp[(K0 + w * P * len(orb) - du, H0 + dz)] += c0 * c1
        pred = newp
    ok_enum = (pred == cnt)
    check(ok_enum, f"{tag}: joint enumerator T6 (brute force vs transfer matrices)")

    # corollaries
    ok_tot = (len(recs) == (P + 1) ** N)
    check(ok_tot, f"{tag}: total count Cor C1")
    lcd = sum(1 for r in recs if r['dimH'] == 0)
    check(lcd == 2 ** len(orbits), f"{tag}: LCD count Cor C3 ({lcd} vs {2**len(orbits)})")
    so = sum(1 for r in recs if r['dimC'] == r['dimH'])
    dc = sum(1 for r in recs if r['dimD'] == r['dimH'])
    check(so == dc, f"{tag}: SO vs DC counts Cor C4 ({so} vs {dc})")
    # SO/DC edge conditions themselves
    ok_edge = True
    inv_map = {tau_img[f]: f for f in facs}
    for r in recs:
        a = dict(zip(facs, r['a']))
        pred_so = all(a[f] + a[inv_map[f]] >= P for f in facs)
        pred_dc = all(a[f] + a[inv_map[f]] <= P for f in facs)
        if pred_so != (r['dimC'] == r['dimH']) or pred_dc != (r['dimD'] == r['dimH']):
            ok_edge = False
    check(ok_edge, f"{tag}: SO/DC edge conditions")

    # means and variance (uniform on labeled assignments)
    tot = len(recs)
    muP = Fraction(P * (2 * P + 1), 6 * (P + 1))
    nuP = Fraction((P * P) // 4, P + 1)
    mean_pred = Fraction(0)
    for orb in orbits:
        if len(orb) == 1:
            mean_pred += nuP * weights[orb[0]]
        else:
            mean_pred += muP * weights[orb[0]] * len(orb)
    mean_act = Fraction(sum(r['dimH'] for r in recs), tot)
    check(mean_pred == mean_act, f"{tag}: mean hull formula ({mean_pred} vs {mean_act})")
    meanC_pred = Fraction(sum(weights[f] * P for f in facs), 2)
    meanC_act = Fraction(sum(r['dimC'] for r in recs), tot)
    check(meanC_pred == meanC_act, f"{tag}: mean dimension formula")
    var_act = Fraction(sum((r['dimH'] - mean_act) ** 2 for r in recs), tot)

    # --- Theorem C6 (variance) and Corollary "second-order structure"
    def V_of(L):
        if L == 1:
            if P % 2 == 0:
                return Fraction(P * (P + 2) * (P * P + 2 * P + 4), 48 * (P + 1) ** 2)
            return Fraction((P - 1) * (P + 3), 48)
        if L == 2:
            return Fraction(P * (P + 2) * (P * P + 2 * P + 3), 18 * (P + 1) ** 2)
        return Fraction(L * P * (P + 2) * (P * P + 2 * P + 2), 60 * (P + 1) ** 2)
    var_pred = sum((weights[orb[0]] ** 2) * V_of(len(orb)) for orb in orbits)
    check(var_pred == var_act, f"{tag}: variance formula C6 ({var_pred} vs {var_act})")
    varC_pred = Fraction(P * (P + 2), 12) * sum(weights[f] ** 2 for f in facs)
    varC_act = Fraction(sum((r['dimC'] - meanC_act) ** 2 for r in recs), tot)
    check(varC_pred == varC_act, f"{tag}: Var(dim C) formula")
    cov_act = Fraction(sum((r['dimC'] - meanC_act) * (r['dimH'] - mean_act) for r in recs), tot)
    check(cov_act == 0, f"{tag}: Cov(dim C, dim Hull) != 0 ({cov_act})")
    res.update(status="ok", mean=float(mean_act), var=float(var_act),
               lcd=lcd, so=so, dc=dc, all_ok=not FAILS)
    return res


def inv_tau_f(facs, tau_img):
    inv = {tau_img[f]: f for f in facs}
    return lambda f: inv[f]


def transfer_trace(P, w, L):
    n = P + 1
    def matmul(A, B):
        O = [[{} for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                acc = {}
                for l in range(n):
                    for (e1, e2), c1 in A[i][l].items():
                        for (f1, f2), c2 in B[l][j].items():
                            key = (e1 + f1, e2 + f2)
                            acc[key] = acc.get(key, 0) + c1 * c2
                O[i][j] = acc
        return O
    T = [[{(w * (P - b), w * min(P - b, a)): 1} for b in range(n)] for a in range(n)]
    R = [[{(0, 0): 1} if i == j else {} for j in range(n)] for i in range(n)]
    for _ in range(L):
        R = matmul(R, T)
    out = Counter()
    for i in range(n):
        for key, c in R[i][i].items():
            out[key] += c
    return out


CASES = [
    # p, d, modulus, k, P, n0, lambda, m_s   (e=1 so m_s = d_s; P = p^nu)
    (3, 1, (0, 1), 0, 1, 4, 1, 1),      # cyclic, P=1, includes a degree-2 factor
    (3, 1, (0, 1), 0, 3, 2, 1, 1),      # P=3, n=6
    (3, 1, (0, 1), 0, 3, 4, 1, 1),      # P=3, n=12
    (5, 1, (0, 1), 0, 5, 2, 4, 1),      # negacyclic lam=-1, P=5, n=10
    (5, 1, (0, 1), 0, 5, 4, 4, 1),      # lam=-1, P=5, n=20, degree-2 factors
    (2, 2, (1, 1, 1), 1, 2, 3, 1, 2),   # F_4, sigma nontrivial (k=1), n=6
    (2, 2, (1, 1, 1), 0, 2, 3, 1, 2),   # F_4, k=0
    (2, 2, (1, 1, 1), 1, 4, 3, 1, 2),   # F_4, P=4
    (3, 2, (1, 0, 1), 1, 3, 2, 1, 2),   # F_9, k=1, P=3, n=6
    (3, 2, (1, 0, 1), 1, 1, 4, 1, 2),   # F_9, k=1, P=1
]


def main():
    cap = 60000
    if '--cap' in sys.argv:
        cap = int(sys.argv[sys.argv.index('--cap') + 1])
    print("=" * 78)
    print("INDEPENDENT VERIFICATION — definition-level dual/hull vs. paper formulas")
    print("=" * 78)
    summary = []
    for c in CASES:
        try:
            r = run_component(*c)
        except AssertionError as e:
            r = dict(tag=str(c[:1] + c[3:]), status=f"ASSERTION: {e or 'internal'}")
        except Exception as e:
            r = dict(tag=str(c), status=f"{type(e).__name__}: {e}")
        r.pop('recs', None)
        summary.append(r)
        print(" ", json.dumps(r, default=str)[:400])
    print("-" * 78)
    bad = [r for r in summary if r.get('status') != 'ok']
    print(f"cases={len(summary)} non-ok={len(bad)} failed_checks={len(FAILS)}")
    if FAILS or bad:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == '__main__':
    sys.exit(main())
