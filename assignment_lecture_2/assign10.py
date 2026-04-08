# lets create a Number guessing game. given a secret number 
# (already decided by you), write a program that asks the user to guess it and 
# prints.

'''
* "too high"  if the guess is above the number 
* "too low " if the guess is below the number 
* "correct" if the guess matches
'''

def Number_guessing_game(n):
    decided_number = 45
    while True:
        if n < 0:
            return "enter number above ", n
      
        if n > decided_number:
            print("too high")
            print(Number_guessing_game(n=int(input("try another number : "))))   
            
        if n<decided_number:
            print("too low")
            print(Number_guessing_game(n=int(input("try another number : ")))) 
        if n == decided_number     
        return "correct"
        break
    return ""
        

print(Number_guessing_game(n=int(input("enter the number : "))))            


# def number_guessing_game():
#     decided_number = 45

#     while True:
#         n = int(input("Enter the number: "))

#         if n < 0:
#             print("Enter number above 0")
#             continue

#         if n > decided_number:
#             print("Too high")

#         elif n < decided_number:
#             print("Too low")

#         else:
#             print("Correct")
#             break


# number_guessing_game()