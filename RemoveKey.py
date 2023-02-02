# WAP to remove a key from a dictionary


def rem(s):
    if s in student:
        del student[stud]
        print(f'{s} record deleted')
        print("Modified Dictionary : ", student)

    else:
        print(f'{s} record not found')


student = {"Alice": 24, "Bob": 21, "Carl": 29, "Aron": 22, "Max": 21, "Heather": 21}

print("Original Dictionary : ", student)

m = int(input('How many records you want to delete:  '))
for i in range(m):
    stud = input('Enter the name of student to delete the record: ')
    try:
        rem(stud)
    except:
        print('Key not found')
