
# Student's Report Card Generator

name = input ("Enter the name of the student :")
roll_number = input ("Enter the roll number of the student :")
maths = float(input ("Enter the marks of  Maths : "))
science = float(input ("Enter the marks of  Science:"))
computerscience = float(input (" Enter the marks of Computer Science: "))

#store student details in a dictionary
student_details = {
    "name": name,
    "roll_number": roll_number,
    "maths": maths,
    "science": science,
    "computerscience": computerscience
}

#calculate total marks and percentage
total_marks = maths + science + computerscience
percentage = (total_marks / 300) * 100  

#decide passed or failed
pass_marks = 40
passed=(
    maths>=pass_marks and science>=pass_marks and computerscience>=pass_marks
)


#assign grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:    grade = "F" 

#nested if with set membership test
remarks = "distinction"

if passed:
    if grade in {"A+", "A"}:
        remarks = "Distinction"
    if grade in {"B", "C"}:
        remarks = "First Class"
    if grade in {"D"}:
        remarks = "Second Class"
    if grade in {"F"}:        
        remarks = "non grade"
else:   
    remarks = "Fail"


status = "Pass" if percentage >= 40 else "Fail"

#display report card

print("\n---- Report Card ----")
print(f"Name: {student_details['name']}")
print(f"Roll Number: {student_details['roll_number']}")

print("\n----------------------")
print(f"Maths: {student_details['maths']}")
print(f"Science: {student_details['science']}")
print(f"Computer Science: {student_details['computerscience']}")

print("\n----------------------")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Status: {status}")
print(f"Remarks: {remarks}")






