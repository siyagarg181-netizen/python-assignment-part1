# Student Grade Tracker Project
# This program cleans data, analyzes marks, and generates reports


# ---------------- TASK 1 ----------------

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("\n--- CLEANED STUDENTS ---\n")

for student in raw_students:
    # cleaning name
    name = student["name"].strip().title()

    # converting roll number
    roll = int(student["roll"])

    # converting marks to list
    marks = [int(x) for x in student["marks_str"].split(", ")]

    # validating name
    valid = all(word.isalpha() for word in name.split())

    if valid:
        print("✓ Valid name:", name)
    else:
        print("✗ Invalid name:", name)

    cleaned_students.append({"name": name, "roll": roll, "marks": marks})

    print("=" * 30)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 30)

# special output
for s in cleaned_students:
    if s["roll"] == 103:
        print("\nSPECIAL CASE (Roll 103):")
        print(s["name"].upper())
        print(s["name"].lower())


# ---------------- TASK 2 ----------------

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("\n--- SUBJECT ANALYSIS ---\n")

def get_grade(m):
    if m >= 90:
        return "A+"
    elif m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 60:
        return "C"
    else:
        return "F"

for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]} ({get_grade(marks[i])})")

total = sum(marks)
average = round(total / len(marks), 2)

print("\nTotal:", total)
print("Average:", average)

# highest & lowest
max_marks = max(marks)
min_marks = min(marks)

print("Highest:", subjects[marks.index(max_marks)], max_marks)
print("Lowest:", subjects[marks.index(min_marks)], min_marks)

# while loop
new_count = 0

while True:
    subject = input("\nEnter subject (or 'done'): ")

    if subject.lower() == "done":
        break

    try:
        score = int(input("Enter marks: "))

        if score < 0 or score > 100:
            print("Invalid marks!")
            continue

        subjects.append(subject)
        marks.append(score)
        new_count += 1

    except:
        print("Invalid input!")

new_avg = round(sum(marks) / len(marks), 2)

print("\nNew subjects added:", new_count)
print("Updated average:", new_avg)


# ---------------- TASK 3 ----------------

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\n--- CLASS REPORT ---\n")

pass_count = 0
fail_count = 0
averages = []

print("Name              | Average | Status")
print("-" * 40)

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    averages.append(avg)

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    print(f"{name:<18} | {avg:^7} | {status}")

print("\nPassed:", pass_count)
print("Failed:", fail_count)

topper = averages.index(max(averages))
print("Topper:", class_data[topper][0], max(averages))

class_avg = round(sum(averages) / len(averages), 2)
print("Class Average:", class_avg)


# ---------------- TASK 4 ----------------

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()

print("\n--- STRING OPERATIONS ---\n")

print("Title Case:\n", clean_essay.title())

print("\nCount of python:", clean_essay.count("python"))

print("\nReplaced:\n", clean_essay.replace("python", "Python 🐍"))

sentences = clean_essay.split(". ")
print("\nSentences List:", sentences)

print("\nNumbered Sentences:")
for i, s in enumerate(sentences, 1):
    if not s.endswith("."):
        s += "."
    print(f"{i}. {s}")