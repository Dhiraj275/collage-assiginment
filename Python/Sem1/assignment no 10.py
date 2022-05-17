marks = float(input("Enter your Percentage: "))
if(marks>=90):
    grade = "A"
elif(marks>=75):
    grade = "B"
elif(marks>=60):
    grade = "C"
elif(marks>=35):
    grade = "D"
else:
    grade =  "F"
print("Student grades are: ", grade)