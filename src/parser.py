import csv

def load_mentors(file_path):
    mentors = {}
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            mentors[row['MentorID']] = {
                'name': row['Name'],
                'domain': row['Domain'],
                'projects': row['Projects'].split(',')
            }
    return mentors


def load_students(file_path):
    students = {}
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            students[row['StudentID']] = {
                'project': row['ProjectID'],
                'completed': int(row['MilestonesCompleted']),
                'total': int(row['TotalMilestones'])
            }
    return students


def load_interactions(file_path):
    interactions = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            interactions.append({
                'mentor_id': row['MentorID'],
                'student_id': row['StudentID'],
                'meetings': int(row['Meetings']),
                'reviews': int(row['CodeReviews']),
                'messages': int(row['Messages']),
                'response_time': float(row['AvgResponseTime'])
            })
    return interactions

def load_feedback(file_path):
    feedback={}
    with open(file_path, 'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            mentor_id = row['MentorID']
            rating = int(row['Rating'])
            
            if mentor_id not in feedback:
                feedback[mentor_id] = []
            
            feedback[mentor_id].append(rating)
    return feedback
