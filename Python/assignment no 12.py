N=int(input("Enter your number:"))
print("Even number from 1 to",N,"are-")
for number in range(1,N+1):
    if(number%2==0):
        print(number)
print(" odd number from 1 to",N,"are-")
for number in range (1,N+1):
    if(number%2!=0):
        print(number)
