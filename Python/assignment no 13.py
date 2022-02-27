num=int(input("Enter a number:"))
Flag=False
#Prime are greate than 1
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            Flag=True
            break
#Flag is true if no is divisible by no other than 1 and itself
if Flag:
    print(num,"is not a Prime number")
else:
    print(num,"is a prime number") 
