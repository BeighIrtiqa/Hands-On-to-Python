# WAP to find the sum of all salaries of employees


def returnSum(emp):
    s = 0
    for x in emp.values():
        s += int(x)
    return s


max = int(input('Enter the number of records: '))
employees = {}

for i in range(max):
    name = input("Enter employee's name: ")
    salary = input("Enter employee's salary: ")

    employees[name] = salary

# {'Alice': '100', 'Bob': '100', 'Carl': '100'}
print(employees)

print("Sum :", returnSum(employees))
