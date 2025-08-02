'''author:Savio Bijo Thomas
   date=19-11-24
   purpose=familiarizing Tuple'''

fruits=("apple","orange","banana","cherry")
print(fruits[-1])
print(fruits[0])
print(fruits[2])
print(len(fruits))
num=(1,2,3,4,5)
concatination=fruits+num
print(concatination)
repeat_tuple=("hello",)*3
print(repeat_tuple)
print("banana" in fruits)
colours=("red","green","blue","orange")
print(colours[-2:])

#unpack tuple into variables
person=("Alice",35,"Engineer")
name,age,profession=person
print(profession)
