#!/usr/bin/env python3
"""T2(i) executable check: (fg)# = f# g# for random polynomials with f(0) != 0."""
import random, sys
import verify_independent as V

fails = total = 0
for (p, d, poly) in [(2,1,(0,1)), (3,1,(0,1)), (5,1,(0,1)), (2,2,(1,1,1)), (3,2,(1,0,1))]:
    F = V.GF(p, d, poly)
    for k in range(0, d):
        rho = lambda x, k=k: F.pow_(x, p**(d-k))
        rng = random.Random(1000*k + p*10 + d)
        for _ in range(400):
            def rand_poly(deg):
                c = [F.els()[rng.randrange(len(F.els()))] for _ in range(deg)]
                c[0] = next(e for e in F.els() if e != F.zero())
                return tuple(c)
            f = F.monic(rand_poly(rng.randint(1,4)))
            g = F.monic(rand_poly(rng.randint(1,4)))
            total += 1
            if V.tau(F, F.pmul(f,g), rho) != F.pmul(V.tau(F,f,rho), V.tau(F,g,rho)):
                fails += 1
print(f"multiplicativity (fg)# = f# g#: {total} random pairs, {fails} failures")
print("RESULT:", "PASS" if fails == 0 else "FAIL")
sys.exit(0 if fails == 0 else 1)
