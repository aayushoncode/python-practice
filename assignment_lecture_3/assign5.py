'''
# Q crate a dictionary where :
# * keys = student names 
# * values = marks (integer)
# write a menu based program where user passes a key (A,B,C,D)
# depending on the operation they want to perform on the dictionary : 
 
# 1. A - add a student 
# 2. B - update marks 
# 3. C - search for a student 
# 4. D - display all students and marks
# '''


students ={
    "vishal" : 69,
    "ayush"  : 99,
    "ajay"   : 45,
    "neha"   : 78,
    "kriti"  : 88,
    "vashisth" : 87
}

# print(students.)

# for j in students :
#     if j == "ayush":
#         students["ayush"] = 90
#         print(students)


# print(students.get("ayush"))

menu = ["1. A - add a student", 
"2. B - update marks", 
"3. C - search for a student", 
"4. D - display all students and marks",
"enter exit to get out of the program"]

print("the students are : ",students)

for i in menu:
    print(i)

def menu(n):
    if(n=="A" or n=="1" or n=="add a student" or n=="a"):
        students.update({input("enter the name : "):int(input("enter the marks : "))})
        print("updated successfully !")
        
        print(students)
    elif(n=="B" or n=="2" or n=="update marks" or n=="b"):
        student_name = input("enter the student name to update his/her marks : ")
        for i in students :
            if i == student_name:
                students[student_name] = int(input("enter the updated marks : "))
                print("updated successfully !")
                print(students)
    elif(n=="C" or n=="3" or n=="search for a student" or n=="c"):
        searched_student = input("enter name of th student : ")
        for i in students :
            if i == searched_student:
                print(f"yes {searched_student} is present and his/her marks is :" , end='')
                print(students[searched_student])
    elif(n=="D" or n=="4" or n=="display all students and marks" or n=="d"):
        print(students)
    elif(n=="E" or n=="5" or n=="exit" or n=="e"):
        print("program ended")
        return 
    
    else:print("enter the correct key")
    menu(n=input("pass a key to perform desired operation : "))
    
    return ""

    
       


menu(n=input("pass a key to perform desired operation : "))