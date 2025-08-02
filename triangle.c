"""AUTHOR:savio bijo thomas
   date:30-11-24
   purpose:to check whether a triangle is right angled or not"""

side1=int(input("enter the side 1 of the triangle:"))
side2=int(input("enter the side 2 of the triangle:"))
side3=int(input("enter the side 3 of the triangle:"))
def right_angled_triangle():
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        print("its a right angled triangle.")
    else:
        print("not a right angled triangle.")
right_angled_triangle()
