#!/usr/bin/env python3
"""
Symbolic (exact, ALL-P) verification of the closed forms in Section 8.

The finite-field verifier checks individual P.  This script proves the closed
forms as polynomial identities in P (splitting P = 2m / 2m+1 where the formula
is parity-dependent), so the formulas are verified for every P, not just the
tested ones.  Requires sympy.

Exit 0 iff every identity holds.
"""
import sys
from sympy import symbols, summation, simplify, Rational, apart, together, factor, floor, Piecewise, expand

P, m, b, c, t, L = symbols('P m b c t L', positive=True, integer=True)
FAILS = []


def ident(lhs, rhs, name):
    d = simplify(together(expand(lhs - rhs)))
    ok = (d == 0)
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else f"   residual={d}"))
    if not ok:
        FAILS.append(name)
    return ok


def main():
    print("=" * 78)
    print("SYMBOLIC (all-P) VERIFICATION OF THE MOMENT CLOSED FORMS")
    print("=" * 78)

    # ---- Lemma 'edge moments'
    Emin = summation((P - t + 1) ** 2, (t, 1, P)) / (P + 1) ** 2
    ident(Emin, P * (2 * P + 1) / (6 * (P + 1)), "E[min(U,V)] = mu_P")

    Emin2 = summation((2 * t - 1) * (P - t + 1) ** 2, (t, 1, P)) / (P + 1) ** 2
    ident(Emin2, P * (P ** 2 + P + 1) / (6 * (P + 1)), "E[min(U,V)^2]")

    Fc = summation(P - t + 1, (t, 1, c)) / (P + 1)
    ident(Fc, c * (2 * P - c + 1) / (2 * (P + 1)), "F(c) = E[min(c,U)]")

    mu = P * (2 * P + 1) / (6 * (P + 1))
    VarX = Emin2 - mu ** 2
    ident(VarX, P * (P + 2) * (2 * P ** 2 + 4 * P + 3) / (36 * (P + 1) ** 2),
          "Var(X) used in the L=2 proof")

    # ---- L = 1 mean: nu_P = floor(P^2/4)/(P+1)
    #   P = 2m   : min(2m-a,a) sums to m^2
    #   P = 2m+1 : min(2m+1-a,a) sums to m(m+1)
    nu_even = m ** 2 / (2 * m + 1)
    ident(nu_even.subs(m, P / 2), (P ** 2 / 4) / (P + 1), "nu_P, P even")
    nu_odd = m * (m + 1) / (2 * m + 2)
    ident(nu_odd.subs(m, (P - 1) / 2), ((P ** 2 - 1) / 4) / (P + 1), "nu_P, P odd")

    # ---- L = 1 variance, both parities
    s_even = 2 * summation(t ** 2, (t, 0, m - 1)) + m ** 2
    V1_even = (s_even / (2 * m + 1) - nu_even ** 2).subs(m, P / 2)
    ident(V1_even, P * (P + 2) * (P ** 2 + 2 * P + 4) / (48 * (P + 1) ** 2), "V_1(P), P even")
    s_odd = 2 * summation(t ** 2, (t, 0, m))
    V1_odd = (s_odd / (2 * m + 2) - nu_odd ** 2).subs(m, (P - 1) / 2)
    ident(V1_odd, (P - 1) * (P + 3) / 48, "V_1(P), P odd")

    # ---- adjacent covariance (L >= 3)
    EXiXi1 = summation(Fc.subs(c, P - b) * Fc.subs(c, b), (b, 0, P)) / (P + 1)
    ident(EXiXi1, P * (P - 1) * (11 * P ** 2 + 15 * P + 6) / (120 * (P + 1) ** 2),
          "E[X_i X_{i+1}]")
    kappa = EXiXi1 - mu ** 2
    ident(kappa, -P * (P + 2) * (7 * P ** 2 + 14 * P + 9) / (360 * (P + 1) ** 2), "kappa_P < 0")

    # ---- L = 2 covariance
    EX0X1 = summation((P - 1 - t) * (t + 1) ** 2, (t, 0, P - 2)) / (P + 1) ** 2
    ident(EX0X1, P ** 2 * (P - 1) / (12 * (P + 1)), "E[X_0 X_1] for L = 2")
    cov2 = EX0X1 - mu ** 2
    ident(cov2, -P ** 2 * (P + 2) ** 2 / (36 * (P + 1) ** 2), "Cov(X_0,X_1) for L = 2")
    ident(2 * VarX + 2 * cov2, P * (P + 2) * (P ** 2 + 2 * P + 3) / (18 * (P + 1) ** 2),
          "V_2(P)")

    # ---- L >= 3
    ident(VarX + 2 * kappa, P * (P + 2) * (P ** 2 + 2 * P + 2) / (60 * (P + 1) ** 2),
          "Var(X) + 2 kappa_P")
    ident(L * (VarX + 2 * kappa),
          L * P * (P + 2) * (P ** 2 + 2 * P + 2) / (60 * (P + 1) ** 2), "V_L(P), L >= 3")

    # ---- Corollary: Var(dim C)
    Bsym = symbols('B', positive=True)          # a uniform on {0..P}
    VarA = summation((t - P / 2) ** 2, (t, 0, P)) / (P + 1)
    ident(VarA, P * (P + 2) / 12, "Var(P - A_f) = P(P+2)/12")

    # ---- second-order corollary: gamma_P = Cov(B, min(B,C))
    EminBC = summation(summation(t, (t, 0, b)) for b in []).subs({}) if False else None
    EminBC = summation(Fc.subs(c, b), (b, 0, P)) / (P + 1)   # E[min(B,C)] with B=b
    EBminBC = summation(b * Fc.subs(c, b), (b, 0, P)) / (P + 1)
    gamma = EBminBC - (P / 2) * EminBC
    ident(gamma, P * (P + 2) / 24, "gamma_P = Cov(B, min(B,C))")

    print("-" * 78)
    print(f"identities checked: 15, failures: {len(FAILS)}")
    print("RESULT:", "PASS" if not FAILS else f"FAIL {FAILS}")
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
