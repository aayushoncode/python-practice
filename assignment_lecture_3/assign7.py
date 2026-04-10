# write a program that takes a string from the user and prints the number
# of spaces in the string

user_input = input("enter any string : ")
spaces = 0
for i in user_input :
    if i == " ":
        spaces+=1
print(spaces)