mark=int(input(" Enter your Persentage "))
if(mark>=90):
    grade="A"
else:
    if(mark>=70):
     grade="B"
    else:
        if(mark>=50):
         grade="C"
        else:
            if(mark>=40):
             grade="D"
            else:
                grade="F"
print(" Your grade is ", grade)
