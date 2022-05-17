def emp_name(n):
    tuple1=()
    list1=[]
    for i in range(0,n):
        name=input("enter the name of emplyee""\n")
        list1.append(name)
        tuple1=tuple(list1)
    print(tuple1) 
    x=input("enter a emplyee name")  
    for ele in tuple1:
        if x==ele :
            print("employee name is present in tuple")
            
emp_name(n=int(input( "how many numbers you want to enter:")) )       
