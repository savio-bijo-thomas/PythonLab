'''author:Savio Bijo Thomas
   date=19-11-24
   purpose=to construct patterns of stars'''
limit=int(input("enter the limit:"))
for i in range(limit+1):      #increasing triangle
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(limit+1,0,-1):
    for j in range(i):         #decreasing triangle
        print("*",end=" ")
    print()
for i in range(1,limit+1):  #for rows
    for j in range(limit-i): #for spacing
        print(" ",end="")                   #hill pattern
    for k in range(2*i-1): #for stars
            print("*",end="")
    print()

for i in range(limit,0,-1):
    for j in range(limit-i):                #reverse hill pattern
        print(" ",end="")
    for k in  range(2*i-1):
        print("*",end="")
    print()
