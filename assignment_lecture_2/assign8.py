#lets create simple calculator that performs arithmatic operations. 
# create a function calculator(a,b,operation) that performs addition, 
# subtraction, multiplication, division based on operation parameter


def calculator(a,b,operation):
    if (operation == "addition"):
        sum = a+b
        print(sum)
    elif (operation == "subtraction"):
        subtract = a-b
        print(subtract)
    elif(operation== "multiplication"):
        multiply = a*b
        print(multiply)
    elif(operation=="division"):
        divide = a/b
        print(divide)

calculator(a=int(input("enter a : ")),b=int(input("enter b : ")),operation=input("enter the operation you want to perform : "))