# write a function that takes a integer a and b and 
# prints all even no. between them


def printEvenNum(a,b):
    for i in range(a+1,b):
        if (i%2==0):
            print(i)


printEvenNum(a=int(input("enter the starting no. :")),b=int(input("enter the ending no. :")))