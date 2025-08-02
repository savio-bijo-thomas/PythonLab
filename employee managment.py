'''author:Savio Bijo Thomas
   date=19-11-24
   purpose=employee management system using tuple'''

employees=[
    ("edwin","manager",50000),
    ("mark","HR",45000),
    ("john","Clerk",10000),
    ("manual","sales",25000)
]
total_annual_expense=0
for information in employees:
    employee_name,department,salary=information
    if salary>20000:
        print("employees having salary above 20000 are:",employee_name)
    total_annual_expense+=salary
print("total annual expense:",total_annual_expense)
