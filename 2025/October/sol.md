# ⚾ Robot Baseball — Full Count Probability

**Goal**  
Find the probability that an at-bat under optimal play reaches a *full count* (3 balls, 2 strikes).  
Both the batter and pitcher play optimally with respect to expected runs.  

---

## 1. Problem Setup

Each pitch is a simultaneous decision:

| Pitcher | Batter | Outcome |
|----------|---------|----------|
| Ball | Wait | +1 Ball |
| Strike | Wait | +1 Strike |
| Ball | Swing | +1 Strike |
| Strike | Swing | Home run with probability *p*, else +1 Strike |

**End conditions**
- 4 balls → walk → +1 run  
- 3 strikes → strikeout → 0 runs  
- home run → 4 runs  

Quad-A adjusts the home-run probability *p* to maximize the likelihood of reaching (3,2).  

---

## 2. Model Overview

We represent each state as **(balls, strikes)** = (b, s).  
There are 12 possible non-terminal states (b ≤ 3, s ≤ 2).

At each state, the pitcher and batter play a 2×2 zero-sum game:

|             | Wait           | Swing                        |
|--------------|----------------|------------------------------|
| **Ball**     | V(b+1, s)      | V(b, s+1)                    |
| **Strike**   | V(b, s+1)      | 4p + (1−p)·V(b, s+1)         |

where **V(b, s)** is the expected score for the batter under optimal play.

---

## 3. Backward Induction

We solve for **V(b, s)** recursively:

- Terminal values:
  - V(4, s) = 1
  - V(b, 3) = 0
- For all other (b, s):
  - Solve the 2×2 matrix above for its saddle point (mixed equilibrium).

Then, compute **Q(b, s)** = probability of reaching (3,2) from (b, s) using optimal strategies.

---

## 4. Result

Numerical evaluation gives:

| Variable | Description | Value |
|-----------|--------------|-------|
| p* | HR probability that maximizes full-count chance | **0.2269732297** |
| q* | Maximal probability of reaching (3,2) | **0.2959679934** |

**As a percentage (10 decimals):**
