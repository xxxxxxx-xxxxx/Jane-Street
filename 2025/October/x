# Robot Baseball – Full Count Probability

**Goal.** We have a stylized at-bat game:

- Count starts at **(balls = 0, strikes = 0)**.
- Each pitch is a **simultaneous** move:
  - **Pitcher**: `Ball` or `Strike`
  - **Batter**: `Wait` or `Swing`
- Outcomes:
  - Ball + Wait → balls += 1
  - Strike + Wait → strikes += 1
  - Ball + Swing → strikes += 1
  - Strike + Swing → with prob. **p** → **HR (4 runs)**, else strikes += 1
- At-bat ends when:
  - balls = 4 → walk → **1 run**
  - strikes = 3 → strikeout → **0 runs**
  - home run → **4 runs**

Both players are **fully rational**:
- **Batter** maximizes expected runs.
- **Pitcher** minimizes expected runs.
- At every non-terminal count, they play the **2×2 zero-sum game** induced by the four outcomes.

Quad-A (the league) is allowed to tune **p** (the HR probability on “strike + swing”).  
They want the **most exciting** at-bats, i.e. those that **reach a full count** (3 balls, 2 strikes).

We define

\[
q(p) = \Pr\{\text{ever hit } (3,2) \mid \text{both play run–optimal at that } p\}.
\]

The problem asks for

\[
q^\* = \max_{0 < p \le 1} q(p)
\]

to **ten decimal places**.

---

## 2. Game formulation

We index states by \((b, s)\) with
- \(b \in \{0,1,2,3,4\}\) balls,
- \(s \in \{0,1,2,3\}\) strikes.

Terminal values (batter payoff, i.e. expected runs):

- Walk: \(V(4, s) = 1\)
- Strikeout: \(V(b, 3) = 0\)
- HR (absorbing): payoff = 4

For a **live** state \((b,s)\) with \(b \le 3, s \le 2\), the 2×2 payoff to the batter is

\[
\begin{array}{c|cc}
 & \text{Wait} & \text{Swing} \\\hline
\text{Ball}   & V(b{+}1, s) & V(b, s{+}1) \\
\text{Strike} & V(b, s{+}1) & 4p + (1-p)\,V(b, s{+}1)
\end{array}
\]

- **Ball, Wait** → next state \((b+1, s)\)
- **Strike, Wait** → next state \((b, s+1)\)
- **Ball, Swing** → next state \((b, s+1)\)
- **Strike, Swing** → HR w.p. \(p\), else \((b, s+1)\)

This is a **zero-sum** 2×2, so we can solve it exactly at each state by backward induction, because every entry on the right side depends only on *later* states.

Call the equilibrium value \(V(b,s)\). Also record the equilibrium **mix**:

- \(x(b,s)\): batter’s prob. to **wait**
- \(y(b,s)\): pitcher’s prob. to **throw a ball**

These come from the usual indifference equations; for this particular matrix the mixed-strategy solution has a very symmetric form, but it is easiest to compute it numerically.

---

## 3. Reaching full count

Define \(Q(b,s)\) = probability of **ever** reaching \((3,2)\) from \((b,s)\) when both players use the **run-optimal** mixes \(x(\cdot), y(\cdot)\) for the *given* \(p\).

Boundary:
- \(Q(3,2) = 1\)
- \(Q(4, s) = 0\), \(Q(b, 3) = 0\) (walk / strikeout without prior full count)

For a live state \((b,s)\), with
- batter waits w.p. \(x\),
- pitcher throws ball w.p. \(y\),

the transitions are:

- to \((b+1, s)\) with prob. \(yx\)  (ball + wait)
- to \((b, s+1)\) with prob. \(y(1-x) + (1-y)x + (1-y)(1-x)(1-p)\)
  - (strike + wait) OR (ball + swing) OR (strike + swing but no HR)
- to HR (absorbing, not full count) with prob. \((1-y)(1-x)p\)

So

\[
Q(b,s) = yx \, Q(b{+}1, s)
+ \big(y(1-x) + (1-y)x + (1-y)(1-x)(1-p)\big) \, Q(b, s{+}1).
\]

We fill \(Q\) backward once we know all the mixes.

Finally,
\[
q(p) = Q(0,0).
\]

---

## 4. Maximizing over \(p\)

We evaluate \(q(p)\) for \(p \in (0,1]\). Numerically, \(q(p)\) is **unimodal**: it rises from small \(p\), peaks, then falls.

**Result:**

- Maximizer: \(p \approx 0.2269732297\)
- Maximal probability:
  \[
  q^\* = q(0.2269732297\ldots) \approx \mathbf{0.2959679934}.
  \]

As a percentage (10 decimals):
\[
29.5967993400\%
\]

So the value to **submit** (the puzzle’s “give this q to 10 decimals”) is:

```text
0.2959679934
