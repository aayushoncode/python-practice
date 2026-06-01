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








