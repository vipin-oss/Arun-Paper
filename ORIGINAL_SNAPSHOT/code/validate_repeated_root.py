#!/usr/bin/env python3
"""
Prototype validation for repeated-root k-Galois hull enumeration.

Single-component examples over GF(4) (and its GF(2) subcase), lambda = 1,
n = P*n0 with P = 2.  For every exponent assignment
    g = prod_f f^{a_f},   a_f in {0,1,2},
we compute (dim C, dim Hull_k(C)) in three independent ways:

 1. VECTOR BRUTE FORCE: generator-matrix basis, code-first Galois dual
    (conjugate of Euclidean dual), intersection dimension by ranks.
 2. EXPONENT FORMULA (proposed theorem):
      hull contribution of a tau-orbit position i:
          min(P - a_i, a_{i-1}) * (factor degree)
 3. TRANSFER TRACE:  tr( T^{L} ) with the (P+1)-state matrix
          T_{a,b} = u^(P-b) z^{min(P-b, a)}   (w=1 here)

GF(4) = {0,1,w,1+w}, w^2 = w+1, encoded as 2-bit ints (XOR = addition).
"""
from itertools import product as cartesian

# ---------- GF(4) arithmetic ----------
def gf_add(a,b): return a^b
def gf_mul(a,b):
    r=0
    while b:
        if b&1: r^=a
        b>>=1; a<<=1
        if a&4: a^=0b111   # x^2 = x+1
    return r
def gf_pow(a,e):
    r=1
    for _ in range(e): r=gf_mul(r,a)
    return r
def gf_inv(a): return gf_pow(a,2)          # a^3=1 for a!=0 in GF(4)
def frob(a):                               # a -> a^2 (identity on GF(2) elements)
    return a if a in (0,1) else (3 if a==2 else 2)

# ---------- polynomials over GF(4): tuple low->high, trimmed ----------
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return tuple(p)
def pmul(p,q):
    # coefficient addition in GF(4) is XOR
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        if a:
            for j,b in enumerate(q):
                if b: r[i+j]^=gf_mul(a,b)
    return trim(r)
def pdivmod(p,q):
    p=list(p); dq=len(q)-1; lc=q[-1]
    quo=[0]*max(1,(len(p)-dq))
    while len(p)-1>=dq and any(p):
        d=(len(p)-1)-dq; c=gf_mul(p[-1],gf_inv(lc))
        if len(quo)<=d: quo.extend([0]*(d-len(quo)+1))
        quo[d]=c
        for j in range(dq+1): p[d+j]^=gf_mul(c,q[j])
        p=list(trim(p))
        if len(p)-1<dq: break
    return trim(quo), trim(p)
def pmod(p,q): return pdivmod(p,q)[1]
def ppow(p,e):
    r=(1,)
    for _ in range(e): r=pmul(r,p)
    return r
def reciprocal_sharp(f):
    """f^# with rho = Frobenius a->a^2, normalized monic."""
    r=len(f)-1; inv=gf_inv(frob(f[0]))
    out=[0]*(r+1)
    for i,ci in enumerate(f):
        out[r-i]=gf_mul(inv,frob(ci))
    return trim(out)
def monic_polys(deg, coeffs=(0,1,2,3)):
    if deg==0: yield (1,); return
    for low in cartesian(coeffs, repeat=deg):
        yield tuple(low)+(1,)
def factorize_separable(poly):
    """Return sorted list of distinct monic irreducible factors (trial division)."""
    factors=[]; rem=poly
    d=1
    while len(rem)>1:
        found=None
        for cand in monic_polys(d):
            if len(cand)-1>d: continue
            if pmod(rem,cand)==(0,):
                found=cand; break
        if found is None: d+=1; continue
        factors.append(found); rem=pdivmod(rem,found)[0]
    return factors

# ---------- linear algebra over GF(4) ----------
def rank(rows):
    rows=[list(r) for r in rows if any(r)]; rk=0
    if not rows: return 0
    ncol=len(rows[0]); r0=0
    for c in range(ncol):
        piv=next((i for i in range(r0,len(rows)) if rows[i][c]),None)
        if piv is None: continue
        rows[r0],rows[piv]=rows[piv],rows[r0]
        inv=gf_inv(rows[r0][c]); rows[r0]=[gf_mul(v,inv) for v in rows[r0]]
        for i in range(len(rows)):
            if i!=r0 and rows[i][c]:
                fac=rows[i][c]; rows[i]=[gf_add(v,gf_mul(fac,w)) for v,w in zip(rows[i],rows[r0])]
        r0+=1; rk+=1
        if r0==len(rows): break
    return rk
def nullspace_basis(rows,ncol):
    rows=[list(r) for r in rows]; piv_cols=[]; r0=0
    for c in range(ncol):
        piv=next((i for i in range(r0,len(rows)) if rows[i][c]),None)
        if piv is None: continue
        rows[r0],rows[piv]=rows[piv],rows[r0]
        inv=gf_inv(rows[r0][c]); rows[r0]=[gf_mul(v,inv) for v in rows[r0]]
        for i in range(len(rows)):
            if i!=r0 and rows[i][c]:
                fac=rows[i][c]; rows[i]=[gf_add(v,gf_mul(fac,w)) for v,w in zip(rows[i],rows[r0])]
        piv_cols.append(c); r0+=1
        if r0==len(rows): break
    free=[c for c in range(ncol) if c not in piv_cols]; basis=[]
    for fc in free:
        v=[0]*ncol; v[fc]=1
        for i,pc in enumerate(piv_cols): v[pc]=rows[i][fc]
        basis.append(v)
    return basis

def code_dims_bruteforce(g,n):
    """(dim C, dim code-first 1-Galois hull) for C=<g> in GF(4)[x]/(x^n-1), k=1."""
    degg=len(g)-1; basis=[]
    for i in range(n-degg):
        row=[0]*n
        shifted=(0,)*i+g
        for j,c in enumerate(shifted): row[j]=c
        basis.append(row)
    dimC=rank(basis)
    euclid_dual=nullspace_basis(basis,n)
    galois_dual=[[frob(v) for v in row] for row in euclid_dual]  # D = rho(C^perp), rho=frob here
    dimD=len(galois_dual)
    dim_hull=dimC+dimD-rank(basis+galois_dual)
    return dimC,dim_hull

# ---------- polynomial dict arithmetic for transfer matrices ----------
def padd(A,B):
    C=dict(A)
    for k,v in B.items(): C[k]=C.get(k,0)+v
    return {k:v for k,v in C.items() if v}
def pmul_dict(A,B):
    C={}
    for (k1,h1),v1 in A.items():
        for (k2,h2),v2 in B.items():
            C[(k1+k2,h1+h2)]=C.get((k1+k2,h1+h2),0)+v1*v2
    return C
def matmul(A,B):
    n=len(A); C=[[dict() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]: continue
            for j in range(n):
                if B[k][j]: C[i][j]=padd(C[i][j],pmul_dict(A[i][k],B[k][j]))
    return C
def matpow(A,e):
    n=len(A); R=[[{(0,0):1} if i==j else dict() for j in range(n)] for i in range(n)]
    for _ in range(e): R=matmul(R,A)
    return R
def transfer_poly(L,P):
    T=[[dict() for _ in range(P+1)] for _ in range(P+1)]
    for a in range(P+1):
        for b in range(P+1):
            T[a][b]={(P-b, min(P-b,a)):1}
    M=matpow(T,L); out={}
    for a in range(P+1): out=padd(out,M[a][a])
    return out

def run_case(name,n0,P,coeff_note=""):
    n=P*n0
    # x^{n0}-1 over GF(4) (char 2: -1 = +1)
    sep=[0]*(n0+1); sep[0]=1; sep[n0]=1; sep=trim(sep)
    facs=factorize_separable(sep)
    print(f"\n=== {name}: n0={n0}, P={P}, n={n} {coeff_note} ===")
    print("distinct irreducible factors of x^n0-1 (low->high):",facs)
    # tau orbits
    fidx={f:i for i,f in enumerate(facs)}; seen=set(); orbits=[]
    for f in facs:
        if f in seen: continue
        orb=[]; cur=f
        while cur not in seen:
            seen.add(cur); orb.append(cur); cur=reciprocal_sharp(cur)
        orbits.append(orb)
    print("tau-orbits (lengths):",[len(o) for o in orbits])
    # 1) brute force over all exponent assignments
    brute={}
    exponent_records=[]
    for exps in cartesian(range(P+1), repeat=len(facs)):
        g=(1,)
        for f,a in zip(facs,exps): g=pmul(g,ppow(f,a))
        K,H=code_dims_bruteforce(g,n)
        brute[(K,H)]=brute.get((K,H),0)+1
        exponent_records.append((exps,K,H))
    # 2) exponent formula
    formula={}
    for exps,K,H in exponent_records:
        Hf=0
        for orb in orbits:
            idx=[fidx[f] for f in orb]; L=len(idx)
            for i in range(L):
                ai=exps[idx[i]]; aprev=exps[idx[i-1]]
                Hf+=(len(orb[i])-1)*min(P-ai,aprev)
        Kf=n-sum((len(f)-1)*a for f,a in zip(facs,exps))
        assert Kf==K, (exps,Kf,K)
        formula[(Kf,Hf)]=formula.get((Kf,Hf),0)+1
    assert formula==brute, ("formula != brute",formula,brute)
    # 3) transfer trace product over orbits
    transfer={(0,0):1}
    for orb in orbits:
        w=len(orb[0])-1
        loc=transfer_poly(len(orb),P)
        locw={}
        for (K,H),v in loc.items(): locw[(w*K,w*H)]=v
        transfer=pmul_dict(transfer,locw)
    assert transfer==brute, ("transfer != brute",transfer,brute)
    total=sum(brute.values())
    lcd=brute.get((0,0),0) if False else sum(v for (K,H),v in brute.items() if H==0)
    print(f"assignments checked: {total}  (expected {(P+1)**len(facs)})")
    print("joint (K,H) distribution:",dict(sorted(brute.items())))
    print(f"LCD count (H=0): {lcd}   predicted 2^(#orbits) = {2**len(orbits)}")
    assert lcd==2**len(orbits)
    print("OK: brute force == exponent formula == transfer trace")
    return brute

if __name__=="__main__":
    run_case("GF(4), k=1, lambda=1",n0=3,P=2)
    run_case("GF(4), k=1, lambda=1",n0=5,P=2)
    run_case("GF(4), k=1, lambda=1",n0=7,P=2)
    run_case("GF(4), k=1, lambda=1",n0=5,P=4)  # P = 2^2, higher multiplicity
    print("\nALL PROTOTYPE CHECKS PASSED")
