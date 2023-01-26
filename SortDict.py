# WAP to sort a Dictionary

salary = {"John": 45000, "Bill": 30000, "Philip": 40000}
print(salary)
salary_sort = sorted(salary.items(), key=lambda x: x[1])
print(salary_sort)

print(list(salary.values()))
v = sorted(salary.values())
print(v)
