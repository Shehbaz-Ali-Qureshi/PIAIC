print('Welcome to Percentage/Grade Calculator')

english = input("enter your english marks: ")
math = input("enter your math marks: ")
chemistry = input("enter your chemistry marks: ")
urdu = input("enter your urdu marks: ")
science = input("enter your science marks: ")

subject_01 = int(english)
subject_02 = int(math)
subject_03 = int(chemistry)
subject_04 = int(urdu)
subject_05 = int(science)

obtained_marks = subject_01 + subject_02 + subject_03 + subject_04 + subject_05
percentage = (obtained_marks/500)*100
print(f"your percentage is: {percentage} ")
if(percentage >= 80.0):
    grade = "A+"
    print(f"your grade is: {grade} ")
elif(percentage >=70.0 and percentage < 80.0):
    grade = "A"
    print(f"your grade is: {grade} ")
elif(percentage >=60.0 and percentage < 70.0):
    grade = "B"
    print(f"your grade is: {grade} ")
elif(percentage >=50.0 and percentage < 60.0):
    grade = "C"
    print(f"your grade is: {grade} ")
elif(percentage < 50.0):
    grade = "F"
    print(f"your grade is: {grade} ")
else:
    print("try again")