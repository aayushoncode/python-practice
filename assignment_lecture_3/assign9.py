 # given a list, print all elements that appear more than
# once in the list 


list1 = [1,2,2,5,4]

seen = set()
Duplicate = set()
for i in list1:
    if i in seen:
        Duplicate.add(i)
    else :
        seen.add(i)
print(Duplicate)
print(seen)