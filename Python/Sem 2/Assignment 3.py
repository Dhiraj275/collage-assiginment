def cube1(n):
    tuple1=()
    list1=[]
    print("print the cube of 1 to n numbers""\n")
    for i in range(1,n+1):
        x=i*i*i
        print(x)
        list1.append(x)
        tuple1=tuple(list1)
       
    print(tuple1)    
cube1(n=int(input( "how many numbers you want to enter:")) )       
