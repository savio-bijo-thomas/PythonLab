'''author:Savio Bijo Thomas
   date=19-11-24
   purpose=to remove duplicate number from a list'''

list=[]
my_list=[1,2,3,4,5,7,7,4]
for number in my_list :
    if number not in list:
        list.append(number)
print("original list is",my_list)
print("the unique list is",list)
