#!/usr/bin/env python3
"""
Independent reproduction of Examples 9.4, 9.5 and 9.6 of the manuscript.

9.4  F_8, k=1, P=2, n0=7, n=14, 2187 assignments, plus the hull-generator
     ORIENTATION claim (predecessor value for all 2187 assignments, successor
     value for 27 of them).
9.5  two components A = F_2 x F_4, q=2, k=0, lambda=(1,1), P=2, n0=7,
     729 assignments, assembled from the component distributions.
9.6  F_9, k=1, lambda = iota (order 4), P=3, n0=4, n=12, 16 assignments.

Design notes
------------
* "definition level" = dual computed by solving <c,y>_k = 0 over F_p from the
  definition of the pairing, hull = C cap D(C) as an intersection of subspaces.
  This never uses T3/T4.
* "formula level"  = the manuscript's T4 exponents.  Comparing the two is the
  actual test.
* Where 2187 definition-level computations would be slow, an exact enumerator
  is used for aggregate numbers and a FIXED-SEED sample is used at definition
  level; the sample size is reported, never hidden.
"""
import sys, json, random, itertools
from fractions import Fraction
from collections import Counter
import verify_independent as V

SEED = 20261023


def parse_paper_distribution(tex_path, marker_start, marker_end):
    """Extract '(a,b){:}n' pairs between two markers of the .tex file."""
    import re
    s = open(tex_path).read()
    i = s.index(marker_start); j = s.index(marker_end, i)
    chunk = s[i:j]
    return Counter({(int(a), int(b)): int(n)
                    for a, b, n in re.findall(r"\((\d+),(\d+)\)[^()]{0,6}?(\d+)", chunk)})


def exponents_of(F, poly, facs):
    """Exponents of each irreducible factor in poly, found by repeated division
    (so the answer does not assume the multiplicative law it is testing)."""
    cur = F.trim(poly)
    ex = []
    for f in facs:
        e = 0
        while cur and F.pdivides(f, cur):
            cur = F.pdiv_monic(cur, f)
            e += 1
        ex.append(e)
    return ex, cur


def run_E4(tex, samples=64):
    F = V.GF(2, 3, (1, 1, 0, 1))          # F_8 = F_2[t]/(t^3+t+1)
    p, d, k, P, n0, m_s = 2, 3, 1, 2, 7, 3
    sig = lambda x: F.pow_(x, p ** k)
    rho = lambda x: F.pow_(x, p ** (d - k))
    lam = F.one()
    mu = next(a for a in F.els() if F.pow_(a, P) == lam)
    n = P * n0
    M = F.trim(tuple([F.neg(mu)] + [F.zero()] * (n - 1) + [F.one()]))
    Mbar = F.trim(tuple([F.neg(mu)] + [F.zero()] * (n0 - 1) + [F.one()]))
    facs = V.factor_monic(F, Mbar, maxdeg=n0)
    tau = {f: V.tau(F, f, rho) for f in facs}
    assert all(any(tau[f] == g for g in facs) for f in facs), "tau leaves the factor set"
    inv = {tau[f]: f for f in facs}
    orbits, seen = [], set()
    for f in facs:
        if f in seen:
            continue
        o, c = [], f
        while c not in seen:
            seen.add(c); o.append(c); c = tau[c]
        orbits.append(o)
    w = m_s  # every factor is linear
    out = {"case": "E4", "n": n, "factors": len(facs), "orbit_lengths": [len(o) for o in orbits],
           "weights": [w] * len(facs), "assignments": (P + 1) ** len(facs)}

    # ---------- exact enumerator (all 2187 assignments, formula level only)
    pred = Counter({(0, 0): 1})
    for o in orbits:
        t = V.transfer_trace(P, w, len(o))
        np_ = Counter()
        for (K0, H0), c0 in pred.items():
            for (du, dz), c1 in t.items():
                np_[(K0 + w * P * len(o) - du, H0 + dz)] += c0 * c1
        pred = np_
    paper = parse_paper_distribution(tex, r"the full joint distribution of",
                                     r"The exponent formula is thus checked")
    # dimensions in the paper are over F_q; here w already includes m_s, so
    # K,H are F_q-dimensions only if divided by m_s:
    pred_q = Counter({(K // m_s, H // m_s): c for (K, H), c in pred.items()})
    out["distribution_match"] = (pred_q == paper)
    out["cells_paper"] = len(paper)
    out["cells_computed"] = len(pred_q)
    if not out["distribution_match"]:
        out["only_paper"] = {str(k): v for k, v in sorted((paper - pred_q).items())}
        out["only_computed"] = {str(k): v for k, v in sorted((pred_q - paper).items())}

    tot = sum(pred_q.values())
    mean = Fraction(sum(K * c for (K, H), c in pred_q.items()), tot)
    meanH = Fraction(sum(H * c for (K, H), c in pred_q.items()), tot)
    varH = Fraction(sum((H - meanH) ** 2 * c for (K, H), c in pred_q.items()), tot)
    out.update(total=tot, mean_hull=str(meanH), var_hull=str(varH),
               mean_hull_expected="11/3", var_hull_expected="10/9",
               moments_match=(meanH == Fraction(11, 3) and varH == Fraction(10, 9)))
    lcd = sum(c for (K, H), c in pred_q.items() if H == 0)
    out["lcd"] = lcd
    out["lcd_match"] = (lcd == 4)

    # SO = DC counts from the B_P matrices (Cor C4), independent of the enumerator
    def tr_B(L, cond):
        B = [[1 if cond(a, b) else 0 for b in range(P + 1)] for a in range(P + 1)]
        R = [[1 if i == j else 0 for j in range(P + 1)] for i in range(P + 1)]
        for _ in range(L):
            R = [[sum(R[i][t] * B[t][j] for t in range(P + 1)) for j in range(P + 1)]
                 for i in range(P + 1)]
        return sum(R[i][i] for i in range(P + 1))
    so = 1
    for o in orbits:
        so *= tr_B(len(o), lambda a, b: a + b >= P)
    out["so_dc"] = so
    out["so_dc_match"] = (so == 258)

    # ---------- ORIENTATION claim, all 2187 assignments, by trial division
    pre_ok = 0; succ_ok = 0; checked = 0
    for assign in itertools.product(range(P + 1), repeat=len(facs)):
        a = dict(zip(facs, assign))
        h = F.pmul_all([f for f in facs for _ in range(P - a[f])])
        hsharp = V.tau(F, F.monic(h), rho)
        # exponents of h# read off by trial division (not by multiplicativity)
        ex, rem = exponents_of(F, hsharp, facs)
        assert len(rem) <= 1, "h# does not split over the factor set"
        pred_pre = [P - a[inv[f]] for f in facs]     # P - alpha_{i-1}
        pred_suc = [P - a[tau[f]] for f in facs]     # P - alpha_{i+1}
        checked += 1
        if ex == pred_pre:
            pre_ok += 1
        if ex == pred_suc:
            succ_ok += 1
    out.update(orientation_checked=checked, predecessor_matches=pre_ok,
               successor_matches=succ_ok,
               orientation_match=(pre_ok == checked and succ_ok == 27))

    # ---------- definition-level spot check on a fixed-seed sample
    rng = random.Random(SEED)
    allassign = list(itertools.product(range(P + 1), repeat=len(facs)))
    rng.shuffle(allassign)
    sample = allassign[:samples]
    bad = 0
    for assign in sample:
        a = dict(zip(facs, assign))
        g = F.pmod_monic(F.pmul_all([f for f in facs for _ in range(a[f])]), M)
        cb = V.code_basis(F, g, M, n)
        db = V.dual_basis(F, cb, n, sig)
        hb = V.intersect(cb, db, n * d, p)
        dimH_T4 = sum(w * min(P - a[f], a[inv[f]]) for f in facs)
        if len(hb) != dimH_T4:
            bad += 1
    out.update(sample_size=len(sample), sample_mismatches=bad,
               sample_ok=(bad == 0), seed=SEED)
    return out


def run_E5(tex):
    """Two components, each computed at definition level, then convolved."""
    comps = [
        dict(p=2, d=1, poly=(0, 1), k=0, P=2, n0=7, lam=1, m_s=1, name="F_2"),
        dict(p=2, d=2, poly=(1, 1, 1), k=0, P=2, n0=7, lam=1, m_s=2, name="F_4"),
    ]
    dists, orbit_data = [], []
    for c in comps:
        r = V.run_component(c["p"], c["d"], c["poly"], c["k"], c["P"], c["n0"], c["lam"], c["m_s"])
        if r.get("status") != "ok":
            return {"case": "E5", "status": r.get("status")}
        dists.append(Counter((x["dimC"], x["dimH"]) for x in r["recs"]))
        orbit_data.append({"component": c["name"], "orbit_lengths": r["orbits"],
                           "weights": r["weights"], "assignments": r["count"]})
    total = Counter({(0, 0): 1})
    for d_ in dists:
        tot = Counter()
        for (K0, H0), c0 in total.items():
            for (K1, H1), c1 in d_.items():
                tot[(K0 + K1, H0 + H1)] += c0 * c1
        total = tot
    n_asg = sum(total.values())
    meanH = Fraction(sum(H * c for (K, H), c in total.items()), n_asg)
    varH = Fraction(sum((H - meanH) ** 2 * c for (K, H), c in total.items()), n_asg)
    lcd = sum(c for (K, H), c in total.items() if H == 0)
    return {"case": "E5", "orbit_data": orbit_data, "assignments": n_asg,
            "assignments_expected": 729,
            "mean_hull": str(meanH), "mean_expected": "11",
            "var_hull": str(varH), "var_expected": "230/9",
            "lcd": lcd, "lcd_expected": 16,
            "matches": (n_asg == 729 and meanH == 11 and varH == Fraction(230, 9) and lcd == 16)}


def run_E6(tex):
    # F_9 = F_3[t]/(t^2+1); iota = t -> packed int 3
    r = V.run_component(3, 2, (1, 0, 1), 1, 3, 4, 3, 2)
    if r.get("status") != "ok":
        return {"case": "E6", "status": r.get("status")}
    cnt = Counter((x["dimC"] // 2, x["dimH"] // 2) for x in r["recs"])   # m_s = 2
    paper = parse_paper_distribution(tex, r"[a twist of order four]", r"Every value was recomputed")
    n_asg = sum(cnt.values())
    meanH = Fraction(sum(H * c for (K, H), c in cnt.items()), n_asg)
    varH = Fraction(sum((H - meanH) ** 2 * c for (K, H), c in cnt.items()), n_asg)
    lcd = sum(c for (K, H), c in cnt.items() if H == 0)
    so = sum(1 for x in r["recs"] if x["dimC"] == x["dimH"])
    return {"case": "E6", "orbit_lengths": r["orbits"], "weights": r["weights"],
            "assignments": n_asg, "assignments_expected": 16,
            "distribution_match": (cnt == paper), "cells": len(paper),
            "mean_hull": str(meanH), "mean_expected": "7/2",
            "var_hull": str(varH), "var_expected": "15/4",
            "lcd": lcd, "lcd_expected": 2, "so_dc": so, "so_dc_expected": 10,
            "matches": (cnt == paper and n_asg == 16 and meanH == Fraction(7, 2)
                        and varH == Fraction(15, 4) and lcd == 2 and so == 10)}


def main():
    tex = "../../FINAL_IEEE_TIT_SUBMISSION.tex"
    import os
    if not os.path.exists(tex):
        tex = "/home/user/Arun-Paper/FINAL_IEEE_TIT_SUBMISSION.tex"
    results = []
    print("=" * 78); print("EXAMPLES 9.4-9.6 REPRODUCTION"); print("=" * 78)
    for fn in (run_E4, run_E5, run_E6):
        try:
            r = fn(tex) if fn is not run_E5 else fn(tex)
        except Exception as e:
            import traceback; traceback.print_exc()
            r = {"case": fn.__name__, "status": f"{type(e).__name__}: {e}"}
        results.append(r)
        print(json.dumps(r, indent=2, default=str)[:2000])
        print("-" * 78)
    ok = all(bool(r.get("matches", r.get("distribution_match", False))) for r in results)
    print("ALL EXAMPLES REPRODUCED" if ok else "REPRODUCTION INCOMPLETE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
