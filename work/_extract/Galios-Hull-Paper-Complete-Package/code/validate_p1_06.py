#!/usr/bin/env python3
"""
P1-06 moment checks for C5 (mean) and C6 (variance). NEW artifact;
no earlier validation script or output is modified.

Model: one orbit, A_0..A_{L-1} iid Uniform{0..P}, cyclic edge variables
    X_i = min(P - A_i, A_{i-1}),   S_L = sum_i X_i   (indices mod L).
Three layers are compared exactly (fractions.Fraction, no floats):
  (1) direct enumeration of A-tuples (capped at 300k tuples);
  (2) exact finite sums for every building block:
        L=1:  sum_a min(P-a,a),  sum_a min(P-a,a)^2;
        edge: tail sums sum_t Pr(min>=t), sum_t (2t-1) Pr(min>=t);
        adjacent edges (L>=3): (1/(P+1)) sum_b F(P-b) F(b),
              F(c) = E[min(c,U)] = sum_{t=1}^c Pr(U>=t);
        L=2 opposite edges: sum_{s,t>=1} ((P-s-t+1)/(P+1))^2  [s+t<=P];
  (3) proposed closed forms (proved in P1_06_MOMENT_PROOFS_C5_C6.md):
        nu_P  = floor(P^2/4)/(P+1),          mu_P = P(2P+1)/(6(P+1)),
        E[min^2] = P(P^2+P+1)/(6(P+1)),
        Var_edge = P(P+2)(2P^2+4P+3) / (36(P+1)^2),
        Cov_adj  = -P(P+2)(7P^2+14P+9) / (360(P+1)^2),
        Cov_L2   = -P^2(P+2)^2 / (36(P+1)^2),
        Var S_1  = P(P+2)(P^2+2P+4)/(48(P+1)^2)  (P even),
                   (P-1)(P+3)/48                  (P odd),
        Var S_2  = P(P+2)(P^2+2P+3) / (18(P+1)^2),
        Var S_L  = L * P(P+2)(P^2+2P+2) / (60(P+1)^2)   (L>=3).
Also a global assembly check: for weighted independent orbits, the
mean adds with weights w_O and the variance adds with weights w_O^2,
verified against exact convolution of per-orbit distributions and,
for one small case, against direct global enumeration.

WHAT IT CANNOT PROVE: the formulas for general (P, L); independence
of orbits in the code model (a product-measure fact proved in the
accompanying note); anything about codes beyond the exponent model.
Finite checks are evidence for the tested values only.
"""
from fractions import Fraction
from itertools import product as cartesian


# ---------------------------------------------------------- closed forms
def nu(P):
    return Fraction((P * P) // 4, P + 1)


def mu(P):
    return Fraction(P * (2 * P + 1), 6 * (P + 1))


def edge_e2(P):
    return Fraction(P * (P * P + P + 1), 6 * (P + 1))


def var_edge(P):
    return Fraction(P * (P + 2) * (2 * P * P + 4 * P + 3), 36 * (P + 1) ** 2)


def cov_adj(P):
    return -Fraction(P * (P + 2) * (7 * P * P + 14 * P + 9), 360 * (P + 1) ** 2)


def cov_L2(P):
    return -Fraction(P * P * (P + 2) ** 2, 36 * (P + 1) ** 2)


def var_S(P, L):
    if L == 1:
        if P % 2 == 0:
            return Fraction(P * (P + 2) * (P * P + 2 * P + 4), 48 * (P + 1) ** 2)
        return Fraction((P - 1) * (P + 3), 48)
    if L == 2:
        return Fraction(P * (P + 2) * (P * P + 2 * P + 3), 18 * (P + 1) ** 2)
    return Fraction(L * P * (P + 2) * (P * P + 2 * P + 2), 60 * (P + 1) ** 2)


def mean_S(P, L):
    return nu(P) if L == 1 else L * mu(P)


# ---------------------------------------------------------- finite sums
def Ffun(P, c):
    """E[min(c, U)], U uniform on {0..P}, as a tail sum."""
    return sum(Fraction(P - t + 1, P + 1) for t in range(1, c + 1))


def blocks_finite_sums(P):
    n1 = Fraction(sum(min(P - a, a) for a in range(P + 1)), P + 1)
    n2 = Fraction(sum(min(P - a, a) ** 2 for a in range(P + 1)), P + 1)
    e1 = sum(Fraction((P - t + 1) ** 2, (P + 1) ** 2) for t in range(1, P + 1))
    e2 = sum(Fraction((2 * t - 1) * (P - t + 1) ** 2, (P + 1) ** 2)
             for t in range(1, P + 1))
    adj = sum(Ffun(P, P - b) * Ffun(P, b) for b in range(P + 1)) / (P + 1)
    l2 = sum(Fraction((P - s - t + 1) ** 2, (P + 1) ** 2)
             for s in range(1, P + 1) for t in range(1, P + 1)
             if s + t <= P)
    return n1, n2, e1, e2, adj, l2


# ---------------------------------------------------------- enumeration
def orbit_dist(P, L):
    dist = {}
    for A in cartesian(range(P + 1), repeat=L):
        S = sum(min(P - A[i], A[i - 1]) for i in range(L))
        dist[S] = dist.get(S, 0) + 1
    return dist


def dist_mean_var(dist):
    tot = sum(dist.values())
    m = Fraction(sum(s * c for s, c in dist.items()), tot)
    v = Fraction(sum(s * s * c for s, c in dist.items()), tot) - m * m
    return m, v


def main():
    Ps = [1, 2, 3, 4, 5, 8, 9]
    print("=== BUILDING BLOCKS: finite sums vs closed forms ===")
    print("P   nu      mu      E[min^2]  Var_edge   Cov_adj    Cov_L2")
    for P in Ps:
        n1, n2, e1, e2, adj, l2 = blocks_finite_sums(P)
        assert n1 == nu(P), (P, n1, nu(P))
        if P % 2 == 0:
            e2_L1 = Fraction(P * (P * P + 2), 12 * (P + 1))
        else:
            e2_L1 = Fraction(P * (P - 1), 12)
        assert n2 == e2_L1, (P, n2, e2_L1)
        assert n2 - n1 * n1 == var_S(P, 1), (P, "L=1 var")
        assert e1 == mu(P) and e2 == edge_e2(P), (P, "edge moments")
        assert e2 - e1 * e1 == var_edge(P), (P, "edge var")
        assert adj - mu(P) ** 2 == cov_adj(P), (P, adj, cov_adj(P))
        assert l2 - mu(P) ** 2 == cov_L2(P), (P, l2, cov_L2(P))
        print(f"{P:<3} {str(nu(P)):<7} {str(mu(P)):<7} {str(e2):<9} "
              f"{str(var_edge(P)):<10} {str(cov_adj(P)):<10} {str(cov_L2(P))}")
    print("OK: every building block (finite sum == closed form)")

    print("\n=== ONE ORBIT: direct enumeration vs mean/variance formulas ===")
    print("P   L   tuples      mean(brute)  mean(formula)  var(brute)   var(formula)")
    for P in Ps:
        for L in (1, 2, 3, 4, 6):
            if (P + 1) ** L > 300_000:
                print(f"{P:<3} {L:<3} skipped (too many tuples; finite sums above cover it)")
                continue
            dist = orbit_dist(P, L)
            m, v = dist_mean_var(dist)
            assert m == mean_S(P, L), (P, L, m, mean_S(P, L))
            assert v == var_S(P, L), (P, L, v, var_S(P, L))
            print(f"{P:<3} {L:<3} {(P + 1) ** L:<11} {str(m):<12} {str(mean_S(P, L)):<14} "
                  f"{str(v):<12} {str(var_S(P, L))}")
    print("OK: enumeration == closed forms for all tested (P, L)")

    print("\n=== GLOBAL ASSEMBLY (independent weighted orbits) ===")
    # small case: direct global enumeration over all exponent tuples
    P, orbits = 2, [(1, 2), (2, 1), (3, 1)]  # (L, w)
    Ls = [L for L, _ in orbits]
    tot_tuples = (P + 1) ** sum(Ls)
    gdist = {}
    for flat in cartesian(range(P + 1), repeat=sum(Ls)):
        pos, H = 0, 0
        for (L, w) in orbits:
            A = flat[pos:pos + L]
            pos += L
            H += w * sum(min(P - A[i], A[i - 1]) for i in range(L))
        gdist[H] = gdist.get(H, 0) + 1
    gm, gv = dist_mean_var(gdist)
    fm = sum(w * mean_S(P, L) for (L, w) in orbits)
    fv = sum(w * w * var_S(P, L) for (L, w) in orbits)
    assert gm == fm and gv == fv, (gm, fm, gv, fv)
    print(f"P={P}, orbits (L,w)={orbits}: {tot_tuples} global tuples; "
          f"mean brute {gm} == formula {fm}; var brute {gv} == formula {fv}")

    # larger case: exact convolution of per-orbit distributions
    P, orbits = 3, [(1, 2), (2, 1), (3, 3), (6, 1)]
    conv = {0: 1}
    for (L, w) in orbits:
        d = orbit_dist(P, L)
        wd = {}
        for s, c in d.items():
            wd[w * s] = wd.get(w * s, 0) + c
        nxt = {}
        for s0, c0 in conv.items():
            for s1, c1 in wd.items():
                nxt[s0 + s1] = nxt.get(s0 + s1, 0) + c0 * c1
        conv = nxt
    cm, cv = dist_mean_var(conv)
    fm = sum(w * mean_S(P, L) for (L, w) in orbits)
    fv = sum(w * w * var_S(P, L) for (L, w) in orbits)
    assert cm == fm and cv == fv, (cm, fm, cv, fv)
    print(f"P={P}, orbits (L,w)={orbits}: convolution of {sum((P+1)**L for L,_ in orbits)} "
          f"per-orbit tuples; mean {cm} == {fm}; var {cv} == {fv}")
    print("OK: global mean adds with w_O, global variance adds with w_O^2")

    print("\nALL P1-06 MOMENT CHECKS PASSED")


if __name__ == "__main__":
    main()
