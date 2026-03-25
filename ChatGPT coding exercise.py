students = []

num_students = int(input("How many students are there? "))

for n in range(num_students):
    student_name = input("What is the student's name? ")
    num_subjects = int(input("How many subjects are there? "))

    scores = []

    for i in range(num_subjects):
        score = float(input(f"Enter score for {i+1}? "))
        scores.append(score)

    average_score = sum(scores)/num_subjects

    if average_score >= 90:
        result = "A - Pass"
    elif average_score >=80:
            result = "B - Pass"
    elif average_score >=70:
               result = "C - Pass"
    elif average_score >=60:
               result = "D - Pass"
    else:
                   result = "F - Fail"

    students.append({
        "name": student_name,
       "scores": scores,
        "average": average_score,
        "result":result})

print("\n=== Student Results ===")

for student in students:
    print(f"""
Name: {student['name']}
Scores: {student['scores']}
Average: {student['average']:.2f}
Result: {student['result']}
-------------------------
""")