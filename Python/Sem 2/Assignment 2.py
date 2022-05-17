tuple1=()
list1=[]
n=int(input( "how many numbers you want to enter:"))
for i in range(1,n+1):
    ele1=input("enter a item: \n")
    list1.append(ele1)
print(list1)
tuple1=tuple(list1)
print(tuple1)
x=max(tuple1)
y=min(tuple1)
print("maximum number:", x, "\n","minimum number:", y)