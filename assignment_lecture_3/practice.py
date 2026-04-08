# slicing


# word = "python"

# print(word[2:4+1])


# formatting

# a=56
# b=90

# sum = a+b

# print("the sum of {} and {} is {}".format(a,b,sum))



# index based formatting

# a=56
# b=90

# sum = a+b

# print("the sum of {1} and {0} is {2}".format(a,b,sum))

# value based formatting

# print("this is {a} {d} {b} and i am your {c}".format(a="AYUSH",b="SINHA",c="DAD", d="KUMAR"))



# datatypes in python 

"""
*lists
*tuples 
*dictionaries
*sets
"""

# marks = [56,66,77,88,98,100]

# print(len(marks))
# marks[4]=90
# print(marks)

# methods of lists

'''
*l.append()
*l.insert(idx,val)
*l.sort()
*l.reverse()
'''

# countries = ["india","russia","china","newzealand","germany","south africa", ]

# countries.reverse()

# print(countries)
# countries.append("america")

# print(countries)

# countries.insert(1,"france")
# print(countries)

# countries.sort()
# print(countries)


# loops in lists

# num = [10,20,30,40,50,60,70]

# to find the index of value 50
# linear search
# idx=0
# for val in num :
#     if val==50:
#         print(f"the index of value 50 is : {idx}")
#         break
#     idx+=1


# tuples 

# tup = (20,10,10,10,10,20,30,40,50,60)

# print(f"the 1st occurance of 10 is at {tup.index(10)} index")
# print(f"the number of times the 10 : {tup.count(10)} times")
# print(tup)


# dictionary in python

# info = {
#     "name"  : "ayush",
#     "college_name" : "shri shankaracharya professional university",
#     "course" : "BCA",
#     "sub" : ["AI/Ml", "Cyber security", "entreprenurship Development", "software engineering"]

# }
# print(info["name"])
# print(info["college_name"])
# print(info["sub"])



# methods in dictionary

info = {
    "name"  : "ayush",
    "college_name" : "shri shankaracharya professional university",
    "course" : "BCA",
    "sub" : ["AI/Ml", "Cyber security", "entreprenurship Development", "software engineering"]

}

# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("idx"))
# info.update({
#     "city":["bhilai","raipur","bilaspur"]
# })

# print(info)


#methods of sets 

# s = {1,3,4,5,3,5,35,2,52,5,2,24,4,2,5,}
# s1 = {"ayush","ajay","neha","priya","arush","nikita"}

s={1,1,2,4,3,5,6}
s1={1,1,2,4,3,5,7,8,9}

# s.add(56)
# s.remove(24)
# s.clear()
# s.pop()
# u=s.union(s1)
# inter=s.intersection(s1)
# print(inter)

# student enrollments

'''
given a list of tuple with info(name , subject):
*list all unique courses
*list students enrolled in english 
*create dictionary (student, set of courses)
'''



