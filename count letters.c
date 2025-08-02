"""author:Savio Bijo Thomas
   date:30-11-24
   purpose:to count number of upper and lower case letters"""

string=input("enter a string:")
def upper_and_lower_case():
    no_of_lowercase=0
    no_of_upper_case=0
    for i in string:
        if i.isupper():
            no_of_upper_case+=1
        elif i.islower():
            no_of_lowercase+=1
    print(no_of_lowercase)
    print(no_of_upper_case)
upper_and_lower_case()
