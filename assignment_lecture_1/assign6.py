#   write a program to swap values of two numbers entered by the user.

'''
a = input("enter number first ")
b = input("enter number second ")

temp= a 
a= b

b= temp

print("now the first number is  : ", a)
print("now the second number is  : ", b)
'''

#   write a program to swap values of two numbers entered by the user using without temp variable .




a = input("enter number first ")
b = input("enter number second ")

a,b=b,a

print("now the first number is  : ", a)
print("now the second number is  : ", b)