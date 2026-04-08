# write a function to return the sum of digits of a number , n. 

# def cal_sum_of_digits(n):
#     total =0
#     for i in range(len(n)):
#         total= total + int(n[i])
#     return total    
   
   

# print( cal_sum_of_digits(n=input("enter any number : ")))




def calSumOfDigits(n):
    total = 0
    while n>0:
        total+=n%10
        n//=10
    return total   

print(calSumOfDigits(n=int(input("enter the digits you want to add : ")))) 
