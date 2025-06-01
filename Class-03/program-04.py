# Percentage and Grade Calculator

english = input("english marks: ")
urdu = input("urdu marks: ")
math = input("math marks: ")
science = input("science marks: ")
chemistry = input("chemistry marks: ")

subject_01 = int(english)
subject_02 = int(urdu)
subject_03 = int(math)
subject_04 = int(science)
subject_05 = int(chemistry)

obtained_marks = subject_01 + subject_02 + subject_03 + subject_04 + subject_05
percentage = (obtained_marks/500*100)
print(f"percentage is: {percentage}")
if(percentage >= 80):
    grade = "A1"
    print(f"grade is: {grade}") 
elif(percentage >= 70.0 and percentage < 80.0):
    grade = "A"
    print(f"grade is: {grade}")  
elif(percentage >= 60 and percentage > 70): 
    grade = "B"
    print(f"grade is: {grade}")
elif(percentage >= 50):
    grade = "Fail"
    print(f"grade is: {grade}")