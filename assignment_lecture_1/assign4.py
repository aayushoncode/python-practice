#the user enters a string containing a number (eg - "45") . convert it to : 

'''
* an interger 
* a float 
* a string again 
print all thre values with their types

'''

userEnters = "75"

converting_to_integer= int(userEnters)
converting_to_float= float(userEnters)
converting_to_string= str(userEnters)

print(f"the user enter {userEnters} the type is {type(userEnters)} and converted to {converting_to_integer} and the type is : {type(converting_to_integer)}")
print(f"the user enter {userEnters} the type is {type(userEnters)} and converted to {converting_to_float} and the type is : {type(converting_to_float)}")
print(f"the user enter {userEnters} the type is {type(userEnters)} and converted to {converting_to_string} and the type is : {type(converting_to_string)}")


