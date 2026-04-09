# ask the user for a string and check whether it is a panlindrome or not .
'''
a panlindrome is a string which is same when we read it forward and backward.
eg- "madam" , "racecar"
'''

def check_panlindrome(n):
    
        if n == n[::-1]:
            return f"yes {n} is a palindrome "
        else:
            return (f"{n} is not a panlindrome")
        
print(check_panlindrome(n=input("check your word panlindrome or not : ")))        