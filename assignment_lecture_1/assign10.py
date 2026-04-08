'''

take a decimal number as input (like 45.78) and output its: 
* integer part - 45
* fractional part - .78

'''

# deci_num = float(input("enter the decimal number : ")) # 55.6

# integer_part = int(deci_num) # 55
# fractional_part = deci_num-integer_part #55.6 - 55

# print("the integer part : ",integer_part)
# print("the integer part : ",fractional_part)








num=input(("enter the decimal number : "))

integer_part,fractional_part = num.split('.')

print(f"the integer part is : {integer_part} \nthe fractional part is : .{fractional_part}")




