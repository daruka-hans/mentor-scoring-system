import math
from utilities import filter_outliers

def compute_student_progress_score(mentor_id, interactions, students):
    completed_milestones = 0
    total_milestones = 0

    for inter in interactions:
        if inter['mentor_id'] == mentor_id:
            s = students[inter['student_id']]
            completed_milestones += s['completed']
            total_milestones += s['total']

    if total_milestones == 0:
        return 0

    return completed_milestones / total_milestones


def compute_responsiveness_score(mentor_id, interactions):
    times = []

    for inter in interactions:
        if inter['mentor_id'] == mentor_id:
            times.append(inter['response_time'])

    if not times:
        return 0

    avg_time = sum(times) / len(times)

    k = 0.1  # tuning parameter

    return math.exp(-k * avg_time)



def compute_engagement_score(mentor_id, interactions):
    total = 0
    mentees = set()

    for inter in interactions:
        if inter['mentor_id'] == mentor_id:
            mentees.add(inter['student_id'])
            total += (
                inter['meetings'] * 15 +
                inter['reviews'] * 5 +
                inter['messages'] * 1
            )

    if not mentees:
        return 0

    return total / len(mentees)


def normalize_engagement(E, c=80):  #normalize to [0,1]
    return E / (E + c)



def compute_mentee_feedback_score(feedbacks):
    if not feedbacks:
        return 0.5

    feedbacks = filter_outliers(feedbacks)  #Filtering unfair feedback

    n = len(feedbacks)
    avg = sum(feedbacks) / n

    return avg / 5  # normalize to [0,1]


def compute_final_mentor_score(P, R, E, F):
    w1, w2, w3, w4 = 0.4, 0.25, 0.25, 0.10
    return w1*P + w2*R + w3*E + w4*F
