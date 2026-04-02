# Ideation Document – Mentor Scoring System

## 1. Overview

The goal of this system is to evaluate mentor effectiveness using multiple scalable metrics and qualitative feedback. The final score is designed to be fair, normalized, and robust to noise.

---

## 2. Mentor Score Definition

The final score is computed as:

M(m) = w1·P + w2·R + w3·E + w4·F

Subject to:
w1 + w2 + w3 + w4 = 1

### Weights Chosen:

* w1 = 0.40 (Student Progress)
* w2 = 0.25 (Responsiveness)
* w3 = 0.25 (Engagement)
* w4 = 0.10 (Feedback)

### Justification:

* Student progress is the most important indicator of mentor effectiveness (given 40% weightage)
* Engagement reflects mentoring effort and intent of mentor to help and guide (given 25% weightage)
* Responsiveness ensures timely support which is also very important as a mentee should not be stuck on small problems for long hours (given 25% weightage)
* Feedback captures subjective experience of mentees but is weighted lower due to potential bias (given 10% weightage)

---

## 3. Metric Design

### 3.1 Student Progress Score (P)

P = Total milestones completed / Total milestones assigned

* Aggregated across all mentees
* Ensures mentors are evaluated based on actual outcomes

---

### 3.2 Responsiveness Score (R)

R(t) = exp(-k · t_avg)

Where:

* t_avg = average response time (hours)
* k = 0.1 (tuning parameter)

### Justification:

* Exponential decay ensures that slow responses are heavily penalized
* Fast responses are rewarded significantly
* Score remains bounded in (0,1)

---

### 3.3 Engagement Score (E_raw)

E_raw = 15·meetings + 5·reviews + 1·messages

* Meetings are weighted highest (deep interaction)
* Reviews indicate technical guidance so are given significant weightage
* Messages reflect communication frequency and are weighted quite low as even a small discussion may have quite a few messages

#### Normalization:

E = E_raw / (E_raw + c)

Where:

* c = 80 (chosen based on given data in interactions.csv and average value of E_raw as per my chosen weights)

### Justification:

* Based on my chosen weights, E_raw varied in the range (35,235) and average was around 100-120 so a mentor with average E_raw got engagement score in the range (0.55,0.66) which is a good score
* It prevents large engagement values from dominating
* Ensures diminishing returns
* Keeps score bounded within [0,1]

---

### 3.4 Feedback Score (F)

* Based on student ratings (1–5)

#### Method:

* if no feedback data, returns 0.5, considering the fact that generally people don't take it seriously to give rating to an average thing/service so the feedback data of an average mentor may be empty 
* feedback data is passed through filter_outliers function in utilities.py to nullify/remove biased or extreme feedback
* Compute average
* Normalize to [0,1] ( dividing average by 5 )

### Justification:

* Reduces impact of extreme or biased ratings
* Ensures robust estimation of mentor quality

### filter_outliers function

* Designed to detect and nullify biased or extreme feedback
* First it takes the feedback data(if not empty), and calculates a local mean of the data
* Then each rating is compared to the local mean - 
  i. if deviation of rating from mean is in the range (1.5,2.5], the local mean is passed for the mentee instead of his actual rating (nullifies biased rating)
  ii. if deviation of rating from mean is >2.5, the rating is ignored (removes extreme rating)

---

## 4. Normalization Strategy

To ensure fairness across mentors:

* Progress is ratio-based
* Responsiveness is naturally bounded
* Engagement is normalized using scaling
* Feedback is normalized to [0,1]

This prevents bias due to:

* Different number of mentees
* Different interaction volumes

---

## 5. Score Evaluation Over Time

Although the dataset is aggregated, the system can be designed for time-based evaluation.

Let Mt be the score at time t:

Mt+1 = (1 − α)Mt + αM_current

Where:

* α = 0.25

### Justification:

* Recent performance is prioritized
* Past performance is also retained and given considerable weightage (75%) so that recent performance does not overshadow consistency
* Smooth transitions in score

---

## 6. Activity Decay

If a mentor is inactive for two consecutive periods:

M_new = M_old × (1 − d)

Where:

* d = 0.1

### Justification:

* Penalizes inactivity but not very harsh if inactivity for two consecutive periods happens sometime due to some unavoidable reasons
* Prevents outdated scores from persisting as it slowly fades away
* Maintains fairness over time

---

## 7. Handling Feedback Bias

* It is done using filter_outliers function in utilities.py file as described above (improves robustness)
* Prevents manipulation by a few users

---

## 8. Assumptions

* Data is aggregated across the program duration
* All students contribute equally
* Interaction counts are accurate

---

## 9. Conclusion

The proposed system balances multiple aspects of mentoring and ensures a fair, interpretable, and scalable evaluation framework.

