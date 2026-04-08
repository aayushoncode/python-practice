# write a function is_prime(n) that returns True if n is a 
# prime number and False otherwise, using a loop.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True   
print(is_prime(n=int(input("enter no. to check prime or not : "))))