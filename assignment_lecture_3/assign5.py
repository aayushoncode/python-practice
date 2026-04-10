'''
Q crate a dictionary where :
* keys = student names 
* values = marks (integer)
write a menu based program where user passes a key (A,B,C,D)
depending on the operation they want to perform on the dictionary : 
 
1. A - add a student 
2. B - update marks 
3. C - search for a student 
4. D - display all students and marks
'''


students ={
    "vishal" : 69,
    "ayush"  : 99,
    "ajay"   : 45,
    "neha"   : 78,
    "kriti"  : 88,
    "vashisth" : 87
}

# for j in students :
#     if j == "ayush":
#         students["ayush"] = 90
#         print(students)


# print(students.get("ayush"))

menu = ["1. A - add a student", 
"2. B - update marks", 
"3. C - search for a student", 
"4. D - display all students and marks"]




print("the students are : ",students)

for i in menu:
    print(i)

def menu(n):
    if(n=="A" or n==1 or n=="add a student" or n=="a"):
        students.update({input("enter the name : "):int(input("enter the marks : "))})
        return students
    elif(n=="B" or n==2 or n=="update marks" or n=="b"):
        student_name = input("enter the student name to update his/her marks : ")
        for i in students :
            if i == student_name:
                students[student_name] = int(input("enter the updated marks : "))
                return students
        


print(menu(n=input("pass a key to perform desired operation : ")))