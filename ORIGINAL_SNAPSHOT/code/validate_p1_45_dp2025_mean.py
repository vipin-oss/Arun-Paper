"""P1-45: exact-rational check that the hull mean of manuscript Theorem 8.2,
restricted to a single field component, coincides with Debnath-Prakash
[DP2025, Theorem 3.3] (Adv. Math. Commun., doi:10.3934/amc.2025010).

In DP2025 notation: P = p^nu; Delta_t = sum of degrees of the distinct
irreducible factors lying in reciprocal cycles of length a_t, with
sum_t a_t * Delta_t = n0 and n = P * n0.  Their Theorem 3.3 gives

  E_k = n - A * Delta_1 - B * sum_{t>=2} a_t * Delta_t,
  A = (3P+1)/4 - delta_P / (4(P+1))   (delta_P = 1 if P even else 0),
  B = P(4P+5) / (6(P+1)).

The manuscript's Theorem 8.2 for one component reads

  E[dim Hull] = nu_P * Delta_1 + mu_P * sum_{t>=2} a_t * Delta_t,
  mu_P = P(2P+1) / (6(P+1)),  nu_P = floor(P^2/4) / (P+1).

This script checks the two expressions agree exactly (rational arithmetic)
on random Delta-vectors for P = 1..9, and reproduces DP2025 Example 3.6
(P=3, n=21, Delta_1=1, one 2-cycle of degree-3 factors: Delta_2=3 -> 23/4).
"""
import random
from fractions import Fraction as F


def nu(P):
    return F(P * P // 4, P + 1)


def mu(P):
    return F(P * (2 * P + 1), 6 * (P + 1))


def ours(P, deltas):
    return nu(P) * deltas.get(1, 0) + mu(P) * sum(
        a * d for a, d in deltas.items() if a >= 2
    )


def theirs(P, deltas):
    delta_P = 1 if P % 2 == 0 else 0
    A = F(3 * P + 1, 4) - F(delta_P, 4 * (P + 1))
    B = F(P * (4 * P + 5), 6 * (P + 1))
    n = P * sum(a * d for a, d in deltas.items())
    return n - A * deltas.get(1, 0) - B * sum(
        a * d for a, d in deltas.items() if a >= 2
    )


def main():
    random.seed(1)
    count = 0
    for P in range(1, 10):
        for _ in range(200):
            ds = {1: random.randint(0, 5)}
            for a in (2, 3, 4, 6):
                ds[a] = random.randint(0, 4)
            assert ours(P, ds) == theirs(P, ds), (P, ds)
            count += 1
    print(f"DP2025 Thm 3.3 == manuscript Thm 8.2 (one component): OK, {count} cases")
    ex = ours(3, {1: 1, 2: 3})
    print(f"DP2025 Example 3.6 via manuscript mean: {ex} (printed: 23/4)")
    assert ex == F(23, 4)


if __name__ == "__main__":
    main()
