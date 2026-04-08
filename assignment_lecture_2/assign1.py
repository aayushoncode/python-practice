# write a program that takes a salary as input. Using conditional statements, calculate the final 
# tax rate  based on these rules 

'''
* if salary < 30,000 ->5%
* if salary is 30,000-70,000 ->15%
* if salary > 70,000 ->25%
'''


salary = int(input("enter your salary : "))

if(salary < 30000):
    tax =  (5*salary)/100
    print("the deducted tax amount is : ",tax)
elif(salary >= 30000 and salary <= 70000 ):
    tax =  (15*salary)/100
    print("the deducted tax amount is : ",tax)
elif(salary > 70000):
    tax =  (25*salary)/100
    print("the deducted tax amount is : ",tax)




