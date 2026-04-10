# Given a tuple of integers, create:
#•A tuple of all even numbers 
#•A tuple of all odd numbers


given_tuple = (1,2,3,4,5,6)

lEven = []
lOdd = []

for val in given_tuple:
    if val%2==0:
        lEven.append(val)
    else :
        lOdd.append(val)
evenTup= tuple(lEven)
oddTup= tuple(lOdd)
print(f"the even tuple is : {evenTup} and its type is : {type(evenTup)}")
print(f"the odd tuple is : {oddTup} and its type is : {type(oddTup)}")

       






# tup1=(2,3,45,6,4)
# tup2=(2,3,4,6,41,55)

# print(tup1+tup2)