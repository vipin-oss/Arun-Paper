# P1-42 independent edge-case checks (fresh enumeration vs transfer trace).
# For each (P, L, w): enumerate all (P+1)^L assignments, build the joint
# (K, H) distribution, and compare against (i) the trace of the transfer
# matrix power computed by bivariate-polynomial matrix multiplication,
# (ii) the closed mean/variance formulas of Theorems 8.2/8.4 and
# Corollary 8.5 (Var(dim C), Cov = 0), (iii) the K <-> Delta-K symmetry,
# (iv) the LCD count 2 per orbit, and (v) equality of the self-orthogonal
# and dual-containing counts. Exact rational arithmetic throughout.
# Numerical corroboration only; not a proof.
from itertools import product
from fractions import Fraction as F


def enum_dist(P, L, w):
    d = {}
    for a in product(range(P + 1), repeat=L):
        K = w * sum(P - x for x in a)
        H = w * sum(min(P - a[i], a[i - 1]) for i in range(L))
        d[(K, H)] = d.get((K, H), 0) + 1
    return d


def trace_dist(P, L, w):
    def mul(A, B):
        C = {}
        for (i, k), p1 in A.items():
            for (k2, j), p2 in B.items():
                if k != k2:
                    continue
                cell = C.setdefault((i, j), {})
                for (e1, c1) in p1.items():
                    for (e2, c2) in p2.items():
                        key = (e1[0] + e2[0], e1[1] + e2[1])
                        cell[key] = cell.get(key, 0) + c1 * c2
        return C

    T = {(a, b): {(w * (P - b), w * min(P - b, a)): 1}
         for a in range(P + 1) for b in range(P + 1)}
    M = {(i, i): {(0, 0): 1} for i in range(P + 1)}
    for _ in range(L):
        M = mul(M, T)
    out = {}
    for i in range(P + 1):
        for e, c in M.get((i, i), {}).items():
            out[e] = out.get(e, 0) + c
    return out


def mu(P):
    return F(P * (2 * P + 1), 6 * (P + 1))


def nu(P):
    return F((P * P) // 4, P + 1)


def V1(P):
    if P % 2 == 0:
        return F(P * (P + 2) * (P * P + 2 * P + 4), 48 * (P + 1) ** 2)
    return F((P - 1) * (P + 3), 48)


def V2(P):
    return F(P * (P + 2) * (P * P + 2 * P + 3), 18 * (P + 1) ** 2)


def VL(P, L):
    return F(L * P * (P + 2) * (P * P + 2 * P + 2), 60 * (P + 1) ** 2)


def main():
    cases = 0
    for P in (1, 2, 3, 4):
        for L in (1, 2, 3, 4):
            for w in (1, 2, 3):
                cases += 1
                d = enum_dist(P, L, w)
                assert d == trace_dist(P, L, w), ('trace', P, L, w)
                N = sum(d.values())
                assert N == (P + 1) ** L
                EK = F(sum(K * c for (K, H), c in d.items()), N)
                EH = F(sum(H * c for (K, H), c in d.items()), N)
                EKK = F(sum(K * K * c for (K, H), c in d.items()), N)
                EHH = F(sum(H * H * c for (K, H), c in d.items()), N)
                EKH = F(sum(K * H * c for (K, H), c in d.items()), N)
                assert EK == F(P * w * L, 2), ('EK', P, L, w)
                assert EH == w * (nu(P) if L == 1 else L * mu(P)), ('EH', P, L, w)
                varH = V1(P) if L == 1 else (V2(P) if L == 2 else VL(P, L))
                assert EHH - EH * EH == w * w * varH, ('varH', P, L, w)
                assert EKK - EK * EK == F(P * (P + 2), 12) * L * w * w, ('varK', P, L, w)
                assert EKH - EK * EH == 0, ('cov', P, L, w)
                Delta = P * w * L
                for (K, H), c in d.items():
                    assert d[(Delta - K, H)] == c, ('sym', P, L, w)
                assert sum(c for (K, H), c in d.items() if H == 0) == 2, ('lcd', P, L, w)
                so = sum(c for (K, H), c in d.items() if H == K)
                dc = sum(c for (K, H), c in d.items() if H == Delta - K)
                assert so == dc, ('so=dc', P, L, w)
    print(f'ALL P1-42 INDEPENDENT EDGE CHECKS PASSED ({cases} (P,L,w) cases; '
          'trace==enumeration, means, variances, Cov=0, symmetry, '
          'LCD=2/orbit, SO=DC)')


if __name__ == '__main__':
    main()
