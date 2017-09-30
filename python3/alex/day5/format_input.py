#__author__ = "Sawyer"
#date:"2017/6/23"


name = input("name:")
print(name)
age = int(input("age:"))
job = input("job:")
salary = input("salary:")

if salary.isdigit():
    salary = int(salary)
# else:
#     exit("must input digit")

msg = '''
----- info of %s -----
Name:   %s
Age :   %d
Job :   %s
salary: %f
You will be retired in %s years
------- end -------
''' % (name,name ,age ,job ,salary, 65-age )




print(msg)