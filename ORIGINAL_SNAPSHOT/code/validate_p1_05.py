#!/usr/bin/env python3
"""
P1-05 multi-component assembly check (NEW; validate_p1_03.py untouched).

WHAT IT TESTS (finite evidence only, not a proof):
  The labeled two-component assembly behind T6, in the case
      A = GF(2) x GF(4),  q = 2, k = 0, lambda = (1, 1), P = 2, n0 = 7, n = 14.
  Component 1: K1 = GF(2),  m1 = [K1:F2] = 1.
  Component 2: K2 = GF(4),  m2 = [K2:F2] = 2.
  For every pair of exponent assignments (27 x 27 = 729 labeled global
  assignments) the global F_q-dimensions are formed additively,
      dim_Fq C = 1*dim_K1 C1 + 2*dim_K2 C2,   dim_Fq Hull likewise
  (component dimensions themselves are brute-forced independently per
  component by the same Gram-rank code-first computation as
  validate_p1_03.py), and the resulting joint distribution is compared
  against:
    (i)   the convolution of the two component brute distributions;
    (ii)  the T6 product of per-orbit transfer traces with F_q-weights
          w_O = m_s * deg_{K_s}(f_O) over the orbits of BOTH components;
    (iii) C1 total 3^(|F1|+|F2|), C2 code-dimension marginal,
          C3 LCD count 2^(#orbits), C4 self-orthogonal and
          dual-containing counts vs products of closed-walk traces.

WHAT IT CANNOT PROVE: the CRT/A-submodule correspondence, the T5/T6
formulas, or anything beyond this single two-component example
(k = 0, lambda = 1, P = 2). The single-component formulas are input
only through their independent Gram-rank brute force per component.
"""
import sys
from itertools import product as cartesian

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from validate_p1_03 import (GF2m, PrimeField, closed_walks, factor_distinct,
                            pmul, pmul_dict, ppow, rank, sharp,
                            transfer_local)


def component(F, k, lam, P, n0, m_s):
    """Return (records, orbits) with records = list of (dimC_K, dimH_K),
    orbits = list of (L, w_O over F_q) with w_O = m_s * deg f_O."""
    n = P * n0
    assert F.pow(lam, 1 + F.p ** (F.m - k)) == F.one, "incompatible twist"
    mu = next(a for a in F.elements if F.pow(a, P) == lam)
    S = [F.zero] * (n0 + 1)
    S[0] = F.neg(mu)
    S[n0] = F.one
    from validate_p1_03 import trim
    S = trim(F, S)
    facs = factor_distinct(F, S)
    assert {sharp(F, k, f) for f in facs} == set(facs), "tau not a permutation"
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

    records = []
    for exps in cartesian(range(P + 1), repeat=len(facs)):
        g = (F.one,)
        for f, a in zip(facs, exps):
            g = pmul(F, g, ppow(F, f, a))
        degg = len(g) - 1
        dimC = n - degg
        gamma = list(g) + [F.zero] * (n - len(g))
        if dimC == 0:
            dimH = 0
        else:
            Phi = {}
            for delta in range(-(dimC - 1), dimC):
                s_lo = max(0, -delta)
                s_hi = min(degg, degg - delta)
                tot = F.zero
                for s in range(s_lo, s_hi + 1):
                    tot = F.add(tot, F.mul(gamma[s], F.frob(gamma[s + delta], k)))
                Phi[delta] = tot
            N = [[Phi[t - r] for r in range(dimC)] for t in range(dimC)]
            dimH = dimC - rank(F, N)
        records.append((dimC, dimH))
    orbit_info = [(len(o), m_s * (len(o[0]) - 1)) for o in orbits]
    return records, orbit_info, len(facs)


def main():
    P, n0, n = 2, 7, 14
    rec1, orb1, nf1 = component(PrimeField(2), k=0, lam=1, P=P, n0=n0, m_s=1)
    rec2, orb2, nf2 = component(GF2m(2, 0b111), k=0, lam=1, P=P, n0=n0, m_s=2)
    orbits = orb1 + orb2
    print(f"component 1 GF(2): {len(rec1)} assignments, |F|={nf1}, orbits (L,w)={orb1}")
    print(f"component 2 GF(4): {len(rec2)} assignments, |F|={nf2}, orbits (L,w)={orb2}")

    # global brute: additive F_q dimensions over labeled pairs
    brute = {}
    for (c1, h1) in rec1:
        for (c2, h2) in rec2:
            key = (c1 + 2 * c2, h1 + 2 * h2)
            brute[key] = brute.get(key, 0) + 1
    total = sum(brute.values())
    print(f"global labeled assignments: {total} (expected {3 ** (nf1 + nf2)})")

    # (i) convolution of component brute distributions (F_q-scaled)
    conv = {}
    d1, d2 = {}, {}
    for (c, h) in rec1:
        d1[(c, h)] = d1.get((c, h), 0) + 1
    for (c, h) in rec2:
        d2[(2 * c, 2 * h)] = d2.get((2 * c, 2 * h), 0) + 1
    for (k1, v1) in d1.items():
        for (k2, v2) in d2.items():
            key = (k1[0] + k2[0], k1[1] + k2[1])
            conv[key] = conv.get(key, 0) + v1 * v2
    assert conv == brute, "convolution != global brute"
    print("(i) convolution of component distributions == global brute: OK")

    # (ii) T6 product of per-orbit transfer traces with F_q weights
    transfer = {(0, 0): 1}
    for (L, w) in orbits:
        transfer = pmul_dict(transfer, transfer_local(L, P, w))
    assert transfer == brute, "T6 product != global brute"
    print("(ii) T6 product of orbit traces (F_q weights) == global brute: OK")

    # (iii) corollaries at global level
    assert total == (P + 1) ** (nf1 + nf2)
    print(f"(iii) C1 total = (P+1)^(|F1|+|F2|) = {total}: OK")

    marg = {}
    for (K, H), c in brute.items():
        marg[K] = marg.get(K, 0) + c
    c2 = {0: 1}
    for (L, w) in orbits:
        # each of the L factors in the orbit contributes (1 + u^w + u^{2w})
        for _ in range(L):
            nxt = {}
            for e0, v0 in c2.items():
                for j in range(P + 1):
                    nxt[e0 + j * w] = nxt.get(e0 + j * w, 0) + v0
            c2 = nxt
    assert c2 == marg, "C2 marginal mismatch"
    print("(iii) C2 code-dimension marginal == prod_f (1+u^w+u^{2w}): OK")

    lcd = sum(c for (K, H), c in brute.items() if H == 0)
    assert lcd == 2 ** len(orbits), (lcd, len(orbits))
    print(f"(iii) C3 LCD count = 2^#orbits = {lcd} (#orbits={len(orbits)}): OK")

    nFq = n * (1 + 2)  # total F_q-length = n * sum_s m_s = 42
    selforth = sum(c for (K, H), c in brute.items() if H == K)
    dualcont = sum(c for (K, H), c in brute.items() if H == nFq - K)
    so_pred = dc_pred = 1
    for (L, w) in orbits:
        so_pred *= closed_walks(P, L, lambda a, b: a + b >= P)
        dc_pred *= closed_walks(P, L, lambda a, b: a + b <= P)
    assert selforth == so_pred and dualcont == dc_pred, (selforth, so_pred, dualcont, dc_pred)
    print(f"(iii) C4 self-orthogonal {selforth} == prod tr(B^L); "
          f"dual-containing {dualcont} == prod tr(B'^L): OK")

    print("\nALL P1-05 MULTI-COMPONENT ASSEMBLY CHECKS PASSED")


if __name__ == "__main__":
    main()
