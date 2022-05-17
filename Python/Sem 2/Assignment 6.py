tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
x = tuplex[3:5]
print("display tuple between index 3 to 5", x)
x = tuplex[:6]
print("Display tuple start to index 6", x)
x = tuplex[5:]
print("Display tuple from index 5 to end index", x)
x = tuplex[:]
print("Display full tuple",x)
x= tuplex[-8:-4]
print(x)
print("\nTuple after sequence of Element is reversed: ")
print(tuplex[::-1])
print(tuplex[::6])
