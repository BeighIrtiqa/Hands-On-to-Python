# WAP TO REMOVE UNWANTED ELEMENTS IN A LIST

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# items to be removed
unwanted_num = {11, 5}

list1 = [i for i in list1 if i not in unwanted_num]

# printing modified list
print("New list after removing unwanted numbers: ", list1)
