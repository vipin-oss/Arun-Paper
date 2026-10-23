#!/usr/bin/env python3
"""
Audit-fix validator (cloud-audit response).

Checks, using the repository implementation in validate_p1_14.py:

  1. A worked example with lambda != +-1: GF(9), k=1, lambda = iota
     (an element of order 4, compatible since lambda^4 = 1), P=3, n0=4.
     Full Gram-rank brute force vs the T4 exponent formula vs the T6
     transfer product, with all moment/count identities (run_field_case).

  2. Additional field-level cases with P = 4, 8, 9 (audit item M5):
     GF(2) with P=4 and P=8 (n0=3), GF(3) with P=9 (n0=2), again by
     full brute force (run_field_case).

  3. Orientation statements (audit item M2), stated correctly:
     (a) the hull DIMENSION is invariant per assignment under reversing
         an orbit, because min(P-a,b) - min(P-b,a) = b - a telescopes
         around the cycle (checked on all tuples for (P,L)=(2,6),(3,4));
     (b) the hull GENERATOR does see the orientation: on the GF(8)
         case of Example 9.4, the exponent vector of h^# equals the
         predecessor prediction P - alpha_{i-1} for every assignment,
         while the successor prediction agrees only sometimes (counted).

Finite checks are evidence for the tested cases only, not proofs.
"""
import itertools
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import validate_p1_14 as vp
from validate_p1_14 import GF, trim, pmul, ppow, pdivmod, pmod, factor_distinct, sharp

FAILS = []


def check(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("FAIL:", msg)


def main():
    GF9 = GF(3, 2, [1, 0, 1])
    GF2 = GF(2, 1, [0, 1])
    GF3 = GF(3, 1, [0, 1])
    GF8 = GF(2, 3, [1, 1, 0, 1])

    print("=== 1. Worked example with lambda of order 4 (Example 9.6 data) ===")
    iota = 3  # element x of GF(9)=F3[x]/(x^2+1); iota^2 = -1, order 4
    check(GF9.pow(iota, 2) != GF9.one and GF9.pow(iota, 4) == GF9.one,
          "iota must have order 4")
    check(GF9.pow(iota, 1 + 3 ** (2 - 1)) == GF9.one, "compatibility lambda^(1+3)=1")
    vp.run_field_case(GF9, k=1, lam=iota, P=3, n0=4)

    print("\n=== 2. Field-level cases with P = 4, 8, 9 (audit M5) ===")
    vp.run_field_case(GF2, k=0, lam=1, P=4, n0=3)
    vp.run_field_case(GF2, k=0, lam=1, P=8, n0=3)
    vp.run_field_case(GF3, k=0, lam=1, P=9, n0=2)

    print("\n=== 3a. Hull dimension is orientation-invariant per assignment ===")
    for (P, L) in ((2, 6), (3, 4), (2, 1), (4, 3)):
        bad = 0
        for A in itertools.product(range(P + 1), repeat=L):
            pred = sum(min(P - A[i], A[i - 1]) for i in range(L))
            succ = sum(min(P - A[i], A[(i + 1) % L]) for i in range(L))
            if pred != succ:
                bad += 1
        check(bad == 0, f"dimension invariance P={P} L={L}: {bad} mismatches")
        print(f"  (P,L)=({P},{L}): predecessor sum == successor sum on all "
              f"{(P+1)**L} tuples (telescoping identity)")

    print("\n=== 3b. Hull generator sees the orientation (GF(8), Example 9.4 case) ===")
    F, k, P, n0 = GF8, 1, 2, 7
    n = P * n0
    mu = next(a for a in F.elements if F.pow(a, P) == F.one)
    S = [F.zero] * (n0 + 1)
    S[0] = F.neg(mu)
    S[n0] = F.one
    S = trim(F, S)
    facs = factor_distinct(F, S)
    M = [F.zero] * (n + 1)
    M[0] = F.neg(F.one)
    M[n] = F.one
    M = trim(F, M)
    tau = {f: sharp(F, k, f) for f in facs}
    tau_inv = {v: kk for kk, v in tau.items()}
    pred_ok = succ_ok = total = 0
    for exps in itertools.product(range(P + 1), repeat=len(facs)):
        a = dict(zip(facs, exps))
        g = (F.one,)
        for f, e in zip(facs, exps):
            g = pmul(F, g, ppow(F, f, e))
        h = pdivmod(F, M, g)[0]
        hs = sharp(F, k, h)
        actual = {}
        rem = hs
        for f in facs:
            e = 0
            while True:
                q, r = pdivmod(F, rem, f)
                if r == (F.zero,):
                    rem, e = q, e + 1
                else:
                    break
            actual[f] = e
        pred = {f: P - a[tau_inv[f]] for f in facs}
        succ = {f: P - a[tau[f]] for f in facs}
        pred_ok += (actual == pred)
        succ_ok += (actual == succ)
        total += 1
    check(pred_ok == total, f"predecessor generator exponents: {pred_ok}/{total}")
    check(succ_ok < total, "successor reading should NOT always match")
    print(f"  h^# exponent vector == predecessor prediction on {pred_ok}/{total} "
          f"assignments; successor prediction on {succ_ok}/{total}")

    print()
    if FAILS or vp.FAILS:
        print(f"{len(FAILS) + len(vp.FAILS)} CHECK(S) FAILED")
        raise SystemExit(1)
    print("ALL AUDIT-FIX VALIDATION CHECKS PASSED")


if __name__ == "__main__":
    main()
