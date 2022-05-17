dict={1:"geeta", 2:"sita", 3:"neha"}
print("display all the keys of dictionary:",dict.keys())
print("display all the values of dictionary:",dict.values())
print("display dictionary items as tuple:",dict.items())
dict.update({4:"sumit"})
print("display dictionary after adding new item:", dict)
print("delete item from specific position")
print("check if key is exist or not")
if 2 in  dict:
   print("2 is one of the key in dictionary")
dict.pop(1)
print(dict)
print("delete las item:")
dict.popitem()
print(dict)
print("Empty dictionary:",dict.clear())
#del dict
print(dict)
