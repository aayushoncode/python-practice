# ask the user for string and check whether it is panlindrome or not.

# user = input(str("enter the string to check whether it is panlindrome or not : "))
# rev=""
# for i in range(len(user)-1,-1,-1):
#     rev+=user[i]
# check = user==rev
# if check == True:
#     print(f"yes {user} is a palindrome")
# else :
#     print(f"no {user} is not a palindrome")




# now by creating function

def checkPalindrome(s):
    if s == s[::-1]:
        return "panlindrome" 
    else :
       return "not a palindrome"



# Given a list of integer compute the average of all numbers in a list.

# given_list = [20,40,]

# average = sum(given_list)/len(given_list)

# print("average = ",[int( average)])




# Input two lists of integers from the user. Merge them in to one
# list and sort the result



# list1 = []

# input_list1 = int(input("enter the no. of element want to enter : "))

# for i in range(input_list1):
#     input_value1 = int(input("enter the value for first list : "))
#     element = list1.append(input_value1)
# print("the first list is : ",list1)
# list2=[]
# input_list2 = int(input("enter the no. of element want to enter for second list : "))

# for i in range(input_list1):
#     input_value2 = int(input("enter the value for second list : "))
#     element = list2.append(input_value2)

# print(f"list1 : {list1} and list2 : {list2}")

# merge_list = list1 + list2

# merge_list.sort()


# print(f"the sorted final list is : {merge_list}")




# method 2


# user_input_list1=[int(x) for x in input("enter the first list : ").split()]
# user_input_list2=[int(x) for x in input("enter the second list : ").split()]

# combine_sorted_list = user_input_list1 + user_input_list2
# combine_sorted_list.sort()

# print(combine_sorted_list)


# Given a tuple of integers, create:
# •A tuple of all even numbers 
# •A tuple of all odd numbers



# tup = (1,3,4,6,85,6,8,55,44,33,78,35)
# l = []
# l2 = []

# for i in tup :
#    if i%2==0 :
#     l.append(i)
#    else :
#       l2.append(i)

# even_tup = tuple(l) 
# odd_tup = tuple(l2) 
# print(f"the even tup : {even_tup} and odd tup : {odd_tup}")



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



# student = {
#     "aman" : 499,
#     "ayush" : 399,
#     "abhay" : 599,
#     "nishant" : 488,
# }

# data = [
# "A - add a student ","B - update marks" ,
# "C - search for a student ","D - display all students and marks",
# ]



# def menu () :
#     for i in data :
#         print(i)
#     user_input = str(input("enter the key to perform task : "))

#     if user_input == "a" or "A":
#         student.update({str(input("enter the name : ")) : int(input("enter the marks : "))})
#         print("added successfully")
        
#     elif user_input == "d" or "D":
#         print(student.items())
    


# menu()


# given a list :
# create a dictionary that maps each word to its length .
# example :  {"apple": 5, "banana": 6, "kiwi": 4}


# fruits_list = ["apple", "banana", "mango"]

# fruits = {}

# def insert_fruits():
#     for i in fruits_list :
#         fruits.update({i:len(i)})
#     return fruits

# print(insert_fruits())



# write a program that takes a string from the user and prints the number
# of spaces in the string


# def space_counter(s):
#     spaces = 0
#     for i in s:
#         if i == " ":
#             spaces+=1
#     return spaces
# print(space_counter(s=str(input("enter string : "))) )



# write a program to check whether two lists share no common elements.

list1= [5,7,3,9,88,8,6,3]
list2= [2,77,10]

flag = True

for i in list1 : 
    if i in list2:
        flag = False

if flag == False :
    print("yes it shares the common element")
else: print("no")