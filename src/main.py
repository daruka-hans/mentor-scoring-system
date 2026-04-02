from parser import load_mentors, load_students, load_interactions, load_feedback
from scoring import *

mentors = load_mentors('./data/mentors.csv')
students = load_students('./data/students.csv')
interactions = load_interactions('./data/interactions.csv')
feedback_data = load_feedback('./data/feedbacks.csv')

results = []

for mentor_id, mentor in mentors.items():
    P = compute_student_progress_score(mentor_id, interactions, students)
    R = compute_responsiveness_score(mentor_id, interactions)
    E_raw = compute_engagement_score(mentor_id, interactions)
    E = normalize_engagement(E_raw)
    feedbacks = feedback_data.get(mentor_id, [])
    F = compute_mentee_feedback_score(feedbacks)

    score = compute_final_mentor_score(P, R, E, F)

    results.append((mentor_id, mentor['name'], score))

# Sort descending
results.sort(key=lambda x: x[2], reverse=True)

# Assign ranks
ranked = []
for i, r in enumerate(results):
    ranked.append((r[0], r[1], r[2], i+1))

# Write output
with open('./output/mentor_scores.csv', 'w') as f:
    f.write("MentorID,Name,Score,Rank\n")
    for r in ranked:
        f.write(f"{r[0]},{r[1]},{r[2]:.4f},{r[3]}\n")
