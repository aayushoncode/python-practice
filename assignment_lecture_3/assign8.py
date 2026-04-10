# write a program to check whether two lists share no common elements.

list1 = [1,2,3,4,5,6,7,]
list2 = [55,77,85]
flag = True
for i in list1 :
    if i in list2:
     flag = False
    
if flag == False:
   print("yes they share common element")
else:
   print("no they not share common element")