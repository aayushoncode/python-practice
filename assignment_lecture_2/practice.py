# if , elif , else

# make a python program that the person age is eligible for vote or not

# a = int(input("enter your age : "))

# if(a>=18):
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")



# elif

# specify young, teenager, adult according to the age

# person= int(input("enter your age : "))

# if (person >= 13 and person <= 18):
#     print("teenager")
# elif(person<13):
#     print("child")
# else : 
#     print("adult")

# check the input no. is odd or even

# a=int(input("enter your no."))

# if (a%2 == 0):
#     print("even")
# else:
#     print("odd")


# username = input("enter your username : ")
# password = input("enter your password : ")

# if (username == 'admin'  and password == 'pass'):
#     print("user logged in successfully !")
# else : 
#     if username != "admin" :
#         print("wrong username , try again")
#     else : 
#         print("wrong password , try again")




# while loop 

# print 1 to 5 through while loop 


# i = 6

# while i >= 1 :
#     print(i)
#     i =i-1



# print multplication table of any number n.

# n = int(input("enter any no. : "))

# i = 0
# while i<10:
#     i +=1
#     t=n*i
#     print( f"{n} x {i} = {t}")


 # using break and continue

# i=1

# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# print("now the loop is outside")



# using for loop

# a = "hello"

# i=0

# for  i in a :
#     print(i)

# for i in range(5):
#     print(i+1)



# a = "artificial intelligence"

# count =0

# for i in a:
#     if (i == "i"):
#         count+=1
# print("the no. of i in A string is : ", count)




# user can find the no. of character word is writtern in a sentence



# print("a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses.the punishment assigned to a defendant found guilty by a court, or fixed by law for a particular offence.")
# print("find the no. of character used the sentence")

# a = "a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses.the punishment assigned to a defendant found guilty by a court, or fixed by law for a particular offence."

# user = input("enter any character from above sentences : ")
# count=0
# for ch in a :
#     if (user == ch ):
#         count+=1
# print(f"the no. of {user} in a sentence is : {count}")


# count the no. of vowels in the senctece

# sentence = "artificial"
# count=0
# for i in sentence :
#     if (i == "a" or i =="e" or i =="i" or i =="o" or i =="u" ) :
#         count+=1
# print(f"the no. of vowels in the artificial is {count}") 



# using the range 


# for i in range(5):
#     print(i)
# for i in range(1,5):
#     print(i)
# for i in range(0,11,2):
#     print(i)


# sum = 0 

# for i in range (1, 5+1):
#     sum+=i
# print("the sum of the no. is : ", sum)




# user = int(input("enter the range at which you want to add the numbers : "))

# sum = 0

# for i in range(1,user):
#     sum+=i
# print(sum)    


#now using functions in python 

# def sum(a,b):
#     s = a+b
#     return s

# print(sum(17,24))


# taking three no. as input and returing average of the no.



# a = int(input("enter the first no."))
# b = int(input("enter the second no."))
# c = int(input("enter the third no."))

# def average(a,b,c):
#     avg = (a+b+c)/3
#     return avg
# print(average(20,40,40))



# def average():
#     a = int(input("enter the first no."))
#     b = int(input("enter the second no."))
#     c = int(input("enter the third no."))
#     avg = (a+b+c)/3
#     return avg
# print(average())



# lambda function


# add = lambda a,b: a+b
# print(add(5,5))

# average = lambda a,b: (a+b)/2
# print(average(5,5))




# write a function to print the factorial of n


def calc_factorial (n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact

n = int(input ( "enter any no. : "))
print(f"the factorial of {n} is {calc_factorial(n)}")

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))


