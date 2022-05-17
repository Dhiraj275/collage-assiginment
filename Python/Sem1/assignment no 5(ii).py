p = float(input("Principle amount: "))
t = float(input("TIme Period: "))
r = float(input("Rate of intrest: "))
n = float(input("Number of time of time compouding will done: "))
r= r/100
ci= p*(1+r/n)**(n*t)
print("Calculated Amount at the end will: ", ci)
print("Calculated compound intrest at the end will: ",  ci-p)
