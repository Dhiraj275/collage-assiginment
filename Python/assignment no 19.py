my_list = [0,9,7,56,4,45,35,34,5]
flag = False 
for i in my_list:
    if (i==34):
        print('Element Exist')
        flag= True
if(flag == False):
    print("Elemnet Does not exist")