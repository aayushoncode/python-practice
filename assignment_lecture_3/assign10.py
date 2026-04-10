# asks the user for a string and print :

# all unique characters 
# the count of unique characters

user_input = input("enter any string : ")
seen = set()
duplicate = set()
count_char = 0

uni = set()
for i in user_input:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
for i in seen :
    if i not in duplicate:
        uni.add(i)
        count_char+=1
        
print(f"the unique character is {uni} and they are : {count_char}")