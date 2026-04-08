# Design a program to continuosly input a number n from user and print 
# if it is positive or negetive until the user enters "quit"


# def continues_input(n):
#        if(type(n)==int):
#             print("integer is : ",n)
#             while type(n)==int:
#                  continues_input(n=int(input("enter the integer value : ")) or n=int(input("enter the integer value : ")))
#        if(n=="quit"):
#              print("exit")
             
                      
                  
                  
                 
            
# continues_input(n=int(input("enter the integer value : ")) or n=(input("enter the integer value : ")))

def continuos_input():
    while True :
        user_input = input("enter the integer or quit : " )

        if(user_input == "quit"):
            return "exit"
        

        try: 
            n=int(user_input)
            print("the integer is : ", n)
        except:
            print("enter integer or quit")

print(continuos_input())