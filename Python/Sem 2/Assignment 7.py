result = {}  

for i in range(3):  

   print("Enter Details of student No.", i+1)  

   roll_no = int(input("Roll No: "))  

   std_name = input("Student Name: ")  

   marks = int(input("Marks: "))  

   result[roll_no] = [std_name, marks]
   
print(result)  


for student in result:  

    if result[student][1] > 75:  
        print("Student's name who get more than 75 marks is/are",(result[student][0]))
