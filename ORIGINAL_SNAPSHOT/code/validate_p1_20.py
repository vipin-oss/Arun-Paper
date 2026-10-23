#!/usr/bin/env python3
"""P1-20 validation: proposed new consequences of the joint enumerator.

Exact integer polynomial arithmetic only (stdlib). This script checks, on a
finite grid, the concrete identities proved in P1_20_NEW_CONSEQUENCES.md:
  (R1) complement-reversal symmetry  N(K,H) = N(D-K,H) per orbit and globally;
  (R2) restricted self-orthogonal / dual-containing joint enumerators
       (transfer matrices with edge admissibility), incl. H=K on SO tuples
       and H = w*sum(alpha) on DC tuples;
  (R3) LCD conditional law: per-orbit options {0, P*w*L}, global mean/variance;
  (R4) orbit-length recurrence at P=1: s_{L+2} = (1+u)s_{L+1} - u(1-z)s_L;
  (R5) conditional-mean counterexample at P=1,L=3 (Cov=0 but E[H|K] not const).
Computation is evidence only; the proofs are in the P1-20 report.
"""
from fractions import Fraction
from itertools import product

FAILS = []

def check(cond, msg):
    if cond:
        print("ok:", msg)
    else:
        print("FAIL:", msg)
        FAILS.append(msg)

# ---------- bivariate polynomial dicts {(k,h): coeff} ----------
def padd(A, B, sign=1):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, 0) + sign * v
        if out[k] == 0:
            del out[k]
    return out

def pmul(A, B):
    out = {}
    for (k1, h1), v1 in A.items():
        for (k2, h2), v2 in B.items():
            key = (k1 + k2, h1 + h2)
            out[key] = out.get(key, 0) + v1 * v2
    return {k: v for k, v in out.items() if v}

def matmul(A, B):
    n = len(A)
    out = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]:
                continue
            for j in range(n):
                if B[k][j]:
                    out[i][j] = padd(out[i][j], pmul(A[i][k], B[k][j]))
    return out

def matpow(A, e):
    n = len(A)
    # identity
    out = [[{(0, 0): 1} if i == j else {} for j in range(n)] for i in range(n)]
    base = A
    while e:
        if e & 1:
            out = matmul(out, base)
        base = matmul(base, base)
        e >>= 1
    return out

def trace_poly(P, L, w, kind):
    # matrix over Z[u,z], rows a = previous exponent, cols b = current exponent
    M = [[{} for _ in range(P + 1)] for _ in range(P + 1)]
    for a in range(P + 1):
        for b in range(P + 1):
            if kind == "full":
                M[a][b] = {(w * (P - b), w * min(P - b, a)): 1}
            elif kind == "SO":
                if a + b >= P:
                    M[a][b] = {(w * (P - b), w * (P - b)): 1}
            elif kind == "DC":
                if a + b <= P:
                    M[a][b] = {(w * (P - b), w * a): 1}
            else:
                raise ValueError(kind)
    if L == 0:
        return {(0, 0): P + 1}  # tr(I)
    Mp = matpow(M, L)
    out = {}
    for i in range(P + 1):
        out = padd(out, Mp[i][i])
    return out

# ---------- brute-force orbit enumeration ----------
def orbit_brute(P, L, w):
    joint, so, dc = {}, {}, {}
    lcd_by_K = {}
    for alpha in product(range(P + 1), repeat=L):
        K = w * sum(P - x for x in alpha)
        H = w * sum(min(P - alpha[i], alpha[i - 1]) for i in range(L))
        joint[(K, H)] = joint.get((K, H), 0) + 1
        if all(alpha[i - 1] + alpha[i] >= P for i in range(L)):
            if H != K:
                check(False, f"SO tuple has H!=K P={P} L={L} alpha={alpha}")
            so[(K, H)] = so.get((K, H), 0) + 1
        if all(alpha[i - 1] + alpha[i] <= P for i in range(L)):
            if H != w * sum(alpha):
                check(False, f"DC tuple has H!=dual-dim P={P} L={L} alpha={alpha}")
            dc[(K, H)] = dc.get((K, H), 0) + 1
        if H == 0:
            lcd_by_K[K] = lcd_by_K.get(K, 0) + 1
    return joint, so, dc, lcd_by_K

def moments_from_joint(joint):
    tot = sum(joint.values())
    EK = Fraction(sum(k * v for (k, h), v in joint.items()), tot)
    EH = Fraction(sum(h * v for (k, h), v in joint.items()), tot)
    EK2 = Fraction(sum(k * k * v for (k, h), v in joint.items()), tot)
    EH2 = Fraction(sum(h * h * v for (k, h), v in joint.items()), tot)
    EKH = Fraction(sum(k * h * v for (k, h), v in joint.items()), tot)
    varK, varH = EK2 - EK * EK, EH2 - EH * EH
    cov = EKH - EK * EH
    # Var(K+H), Var(K-H) directly
    Ep = Fraction(sum((k + h) ** 2 * v for (k, h), v in joint.items()), tot) - (EK + EH) ** 2
    Em = Fraction(sum((k - h) ** 2 * v for (k, h), v in joint.items()), tot) - (EK - EH) ** 2
    return EK, EH, varK, varH, cov, Ep, Em

def main():
    print("=== R1/R2: orbit grid (symmetry + restricted enumerators) ===")
    for P in (1, 2, 3, 4):
        for L in (1, 2, 3, 4):
            if (P + 1) ** L > 20000:
                continue
            for w in (1, 2):
                joint, so, dc, lcd = orbit_brute(P, L, w)
                D = w * L * P
                sym = all(joint.get((k, h), 0) == joint.get((D - k, h), 0)
                          for (k, h) in list(joint.keys()))
                check(sym, f"R1 symmetry P={P} L={L} w={w}")
                check(trace_poly(P, L, w, "full") == joint,
                      f"full trace = brute P={P} L={L} w={w}")
                check(trace_poly(P, L, w, "SO") == so,
                      f"R2 SO restricted trace = brute P={P} L={L} w={w}")
                check(trace_poly(P, L, w, "DC") == dc,
                      f"R2 DC restricted trace = brute P={P} L={L} w={w}")
                lcd_expect = {0: 1, P * w * L: 1} if P * w * L != 0 else {0: 2}
                check(lcd == lcd_expect, f"R3 per-orbit LCD options P={P} L={L} w={w}")
    print("=== R2 worked example P=2 L=2 w=1 ===")
    joint, so, dc, _ = orbit_brute(2, 2, 1)
    print("SO joint:", dict(sorted(so.items())), " DC joint:", dict(sorted(dc.items())))
    check(so == {(0, 0): 1, (1, 1): 2, (2, 2): 3}, "SO example counts (0,0):1,(1,1):2,(2,2):3")
    check(dc == {(4, 0): 1, (3, 1): 2, (2, 2): 3}, "DC example counts (4,0):1,(3,1):2,(2,2):3")

    print("=== R1 global + R5 conditional counterexample ===")
    # global convolution, P=2, orbits (L,w) = (1,1),(2,1),(1,2)
    P = 2
    config = [(1, 1), (2, 1), (1, 2)]
    gj = {(0, 0): 1}
    for (L, w) in config:
        oj, _, _, _ = orbit_brute(P, L, w)
        gj = pmul(gj, oj)
    D = P * sum(w * L for (L, w) in config)
    check(all(gj.get((k, h), 0) == gj.get((D - k, h), 0) for (k, h) in list(gj.keys())),
          f"R1 global symmetry D={D}")
    EK, EH, varK, varH, cov, Ep, Em = moments_from_joint(gj)
    print(f"global config moments: E[K]={EK} E[H]={EH} VarK={varK} VarH={varH} Cov={cov}")
    check(cov == 0 and Ep == varK + varH and Em == varK + varH,
          "N1/N2 consequence on this config: Cov=0, Var(K+-H)=VarK+VarH")
    # conditional counterexample P=1, L=3, w=1
    j13, _, _, _ = orbit_brute(1, 3, 1)
    tot_by_K = {}
    hsum_by_K = {}
    for (k, h), v in j13.items():
        tot_by_K[k] = tot_by_K.get(k, 0) + v
        hsum_by_K[k] = hsum_by_K.get(k, 0) + h * v
    cond = {k: Fraction(hsum_by_K[k], tot_by_K[k]) for k in sorted(tot_by_K)}
    print("P=1 L=3 conditional E[H|K]:", {k: str(v) for k, v in cond.items()})
    check(cond == {0: Fraction(0), 1: Fraction(1), 2: Fraction(1), 3: Fraction(0)},
          "R5 conditional mean not constant (0,1,1,0) despite Cov=0")

    print("=== R3: LCD conditional law, E5-type configuration ===")
    P = 2
    config = [(1, 1), (2, 3), (1, 2), (2, 6)]
    # brute over all assignments: total exponent count sum L = 6 -> 3^6 = 729
    all_orbits = []
    for (L, w) in config:
        all_orbits.append(list(product(range(P + 1), repeat=L)))
    tot_lcd = 0
    sumK = Fraction(0)
    sumK2 = Fraction(0)
    for combo in product(*all_orbits):
        K = 0
        H = 0
        for (L, w), alpha in zip(config, combo):
            K += w * sum(P - x for x in alpha)
            H += w * sum(min(P - alpha[i], alpha[i - 1]) for i in range(L))
        if H == 0:
            tot_lcd += 1
            sumK += K
            sumK2 += K * K
    mean = sumK / tot_lcd
    var = sumK2 / tot_lcd - mean * mean
    mean_f = Fraction(P, 2) * sum(w * L for (L, w) in config)
    var_f = Fraction(P * P, 4) * sum((w * L) ** 2 for (L, w) in config)
    print(f"LCD count={tot_lcd} mean={mean} var={var} | formulas mean={mean_f} var={var_f}")
    check(tot_lcd == 2 ** len(config) and mean == mean_f and var == var_f,
          "R3 LCD conditional mean/variance formulas")

    print("=== R4: P=1 orbit-length recurrence ===")
    s = [{(0, 0): 2}]  # s_0 = tr(I_2)
    for L in range(1, 9):
        s.append(trace_poly(1, L, 1, "full"))
    one_plus_u = {(0, 0): 1, (1, 0): 1}
    for L in range(0, 7):
        lhs = s[L + 2]
        # rhs = (1+u)s_{L+1} - u(1-z)s_L = (1+u)s_{L+1} - u s_L + u z s_L
        rhs = pmul(one_plus_u, s[L + 1])
        rhs = padd(rhs, {(k + 1, h): v for (k, h), v in s[L].items()}, sign=-1)
        rhs = padd(rhs, {(k + 1, h + 1): v for (k, h), v in s[L].items()})
        check(lhs == rhs, f"R4 recurrence s_{L+2} = (1+u)s_{L+1} - u(1-z)s_L")
    print("s_1 =", dict(sorted(s[1].items())), " s_2 =", dict(sorted(s[2].items())))

    print()
    if FAILS:
        print(f"{len(FAILS)} FAILURES")
        raise SystemExit(1)
    print("ALL P1-20 VALIDATION CHECKS PASSED")

if __name__ == "__main__":
    main()
