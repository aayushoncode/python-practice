# Given a tuple of integers, create:
#•A tuple of all even numbers 
#•A tuple of all odd numbers


given_tuple = (1,2,3,4,5,6)
# print(type(given_tuple))
even_tup = tuple()
tup2=tuple()
for val in given_tuple :
    if val%2==0:
        even_tup= val
        tup2+=even_tup
        print(tup2)
        