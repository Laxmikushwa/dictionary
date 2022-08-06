# Take input of name and marks of 10 students and store to a dictionary.
user=int(input("enter the number="))
e={}
for i in range(user):
    student_name=input("enter the student_name=")
    student_marks=int(input("enter the student_marks="))
    e[student_name]=student_marks
print(e)