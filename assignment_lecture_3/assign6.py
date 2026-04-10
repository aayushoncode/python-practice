# given a list :
# create a dictionary that maps each word to its length .
# example :  {"apple": 5, "banana": 6, "kiwi": 4}

words = ["apple","banana", "kiwi", "cherry", "mango"]
dict_words={}
# print(dict_words)
for i in words:
    dict_words[i] = len(i)
print(dict_words)
    
