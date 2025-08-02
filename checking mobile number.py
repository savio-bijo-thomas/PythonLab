"""AUTHOR:savio bijo thomas
   date:30-11-24
   purpose:to check whether the given number is a valid mobile number or not"""

num=input("enter the mobile number:")
def check_number():
    length=len(num)
    if length==10:
        if num[0]=="7" or num[0]=="8" or num[0]=="9":
            print("the number is valid")
        else:
            print("the number is invalid")
    else:
        print("invalid")
check_number()
