def solve_values_and_strategies(p):
    V = {(4, s): 1.0 for s in range(3)}
    V.update({(b, 3): 0.0 for b in range(4)})
    x, y = {}, {}
    for s in reversed(range(3)):
        for b in reversed(range(4)):
            A = V[(min(b+1,4), s)]
            B = V[(b, min(s+1,3))]
            C = 4*p + (1-p)*B
            denom = A - 2*B + C
            if abs(denom) < 1e-12:
                xb = 1.0 if min(A,B) >= min(B,C) else 0.0
            else:
                xb = (C - B) / denom
                xb = min(max(xb, 0.0), 1.0)
            if 0.0 < xb < 1.0:
                yb = (C - B) / denom
                yb = min(max(yb, 0.0), 1.0)
                val = yb * (xb*A + (1-xb)*B) + (1-yb)*(xb*B + (1-xb)*C)
            else:
                if xb == 1.0:
                    yb = 1.0 if A <= B else 0.0
                    val = min(A, B)
                else:
                    yb = 1.0 if B <= C else 0.0
                    val = min(B, C)
            V[(b, s)] = val
            x[(b, s)] = xb
            y[(b, s)] = yb
    return V, x, y

def reach_full_count_probability(p):
    V, x, y = solve_values_and_strategies(p)
    Q = {(4, s): 0.0 for s in range(3)}
    Q.update({(b, 3): 0.0 for b in range(4)})
    Q[(3, 2)] = 1.0
    for s in reversed(range(3)):
        for b in reversed(range(4)):
            if (b, s) == (3, 2): 
                continue
            xb, yb = x[(b, s)], y[(b, s)]
            to_ball = yb * xb
            to_strike = yb*(1-xb) + (1-yb)*xb + (1-yb)*(1-xb)*(1-p)
            Q[(b, s)] = to_ball * Q[(min(b+1,4), s)] + to_strike * Q[(b, min(s+1,3))]
    return Q[(0, 0)]

# scan for best p
best_p, best_q = None, -1.0
for i in range(1, 2001):
    p = i / 2000.0
    q = reach_full_count_probability(p)
    if q > best_q:
        best_q, best_p = q, p

print("best p:", best_p)
print("max q:", f"{best_q:.10f}")
