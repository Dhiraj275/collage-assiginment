list1= [1,2,3,4,5,1,1]
list2=["a","b","c"]
list3=[1,"a",2,3,"b"]
print("number list:", list1,"\n", "string list:", list2,"\n", "string and number list:", list3)
list1.append(4)
print("Display listitem after adding a item in list1", list1)
list2.extend([1,2,"a","d"])
print("Display listitem after adding multiple item in list2", list2)
list3.insert(2,10)
print("Display listitem after adding a item at specific position in list2",list3)
list2.remove("b")
print("Display listitem after removing b in list2",list2)
list2.pop(1)
print("Display list2 after remove 1st osition item", list2)
list2.clear()
print("Empty the list2", list2)
print("Display the sum of list1 items",sum(list1))
print("Count how many time 1 is occurring in list1",list1.count(1))
print("display the length of the list1",len(list1))
# Access a list
# using index number
print("Display the item on 1st position in list1", list1[1])
print("items in list1 are")
for i in list1:
    print(i)