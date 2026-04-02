# MENTOR SCORING SYSTEM – WnCC SoC


## OVERVIEW:

This project implements a Mentor Scoring System to evaluate mentor effectiveness in WnCC’s Seasons of Code (SoC).

The system computes a final score for each mentor using multiple indicators:

-> Student Progress
-> Responsiveness
-> Engagement
-> Mentee Feedback

Mentors are then ranked based on their scores.


## HOW TO RUN:

1. Clone the repository
    
    ```
    git clone git@github.com:daruka-hans/mentor-scoring-system.git
    cd mentor-scoring-system
    ```

2. Run the program
    
    ```
    python src/main.py
    ```

## PROJECT STRUCTURE:

mentor-scoring-system/
| 
|── data/
|     |── mentors.csv 
|     |── students.csv 
|     |── interactions.csv
|      |── feedbacks.csv  
|
|── src/
|     |── main.py 
|     |── parser.py 
|     |── scoring.py 
|     |── utilities.py 
| 
|── docs/ 
|     |── ideation.md 
| 
|── output/
|
|── README.md 
|── requirements.txt 
|── .gitignore


## OUTPUT:

The program generates-
    output/mentor_scores.csv

Format-
    MentorID,Name,Score,Rank


## CONCLUSION:

This project provides a fair and clean method to assess mentors using both scalable metrics and student feedback.
