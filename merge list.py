'''author:Savio Bijo Thomas
   date=19-11-24
   purpose=Merging two list and sorting them in given condition'''

list1=[]
list2=[]
limit1=int(input("enter the number of elements in list 1:"))
print("enter the elements in list 1:")
for i in range(limit1):
    list1.append(int(input()))
limit2=int(input("enter the number elements in list 2:"))
print("enter the elements in list 2:")
for i in range(limit2):
    list2.append(int(input()))
print("the first list is",list1)
print("the second list is",list2)
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list=even_list+odd_list
print("the merged list is",merged_list)
