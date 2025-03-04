import csv
from collections import defaultdict

grades_data = [
    ["Name", "Subject", "Grade"],
    ["Alice", "Math", "85"],
    ["Bob", "Science", "78"],
    ["Carol", "Math", "92"],
    ["Dave", "History", "74"]
]

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)

print(" 'grades.csv' has been created.")

# Step 2: Read data from grades.csv
grades = defaultdict(list)

with open("grades.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        subject = row["Subject"]
        grade = int(row["Grade"])
        grades[subject].append(grade)

average_grades = {subject: sum(scores) / len(scores) for subject, scores in grades.items()}

with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in average_grades.items():
        writer.writerow([subject, avg])

print(" 'average_grades.csv' has been created with average grades.")
