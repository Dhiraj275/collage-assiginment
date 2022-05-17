Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.count((3))
print('Count of (3) in Tuple is:', res)
  
res = Tuple.count(1)
print('Count of (1) in Tuple is:', res)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
  
res = Tuple.index(3, 4)
print('First occurrence of 3 after 4th index is:', res)
print("length of the tuple", len(Tuple))
print("print minimum value of the tuple",min(Tuple))
print("print max value of the tuple", max(Tuple))
t=Tuple*2
print("tuple multiply by 2", t)
t1= (8,9,10)
t3=Tuple+t1
print("Addition of two tuple is", t3)
t4=(1,2)+(3,4)+t1
print("Addition of tuples", t4)

