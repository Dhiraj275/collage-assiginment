import os
myStr = ""
for i in range(1, 10):
    # f = open(f"Assignmet {i}.py", "a")
    # f.write("")
    # f.close()
    # os.rename(f"E:\Collage Work\Programming\Python\Sem 2\Assignmet {i}.py", f"Assignment {i}.py")
    MyAssignment = open(f"E:\Collage Work\Programming\Python\Sem 2\Assignment {i}.py", "r")
    myStr = myStr +f"\n Assignment {i} \n \n" f"{MyAssignment.read()} \n \n"

AllAssignament = open(f"E:\Collage Work\Programming\Python\Sem 2\All Assignment.txt", "a")
AllAssignament.write(myStr)
