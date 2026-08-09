# Student Grade Calculator

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Get student details
name = input("Enter student name: ")

# Get marks
subjects = ["Python", "AI", "Mathematics", "English", "Computer Science"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = total / len(subjects)

# Calculate grade
grade = calculate_grade(percentage)

# Display result
print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)