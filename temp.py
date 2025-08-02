"""Author:Savio Bijo Thomas
   date-15-10-2024
purpose:Program to convert the unit of temperature"""

temp=int(input("enter the temperture:"))
unit=input("if the temperature is in celsius press 'C' or 'F' for fahrenheit: ")
if unit=="C":
    f=(9/5*temp)+32
    print(temp ,"celsius is",f,"fahrenheit.")
elif unit=="F" :
    c=5/9*(temp-32)
    print(temp,"fahrenheit is",c,"celsius.")
else:
    print("INVALID INPUT")
