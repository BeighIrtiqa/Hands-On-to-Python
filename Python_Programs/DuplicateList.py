def split_lists(input_list):
    duplicate_dict = {}
    unique_list = []
    duplicate_list = []
    for element in input_list:
        if input_list.count(element) > 1:
            if element not in duplicate_list:
                duplicate_list.append(element)
                duplicate_dict[element] = input_list.count(element)
        else:
            unique_list.append(element)

    return unique_list, duplicate_list, duplicate_dict


in_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
un_list, dupe_list, dupe_dict = split_lists(in_list)
print("Unique List: ", un_list)
print("Duplicate List: ", dupe_list)

occur = input('PRESS y TO CHECK THE OCCURRENCE OF THE DUPLICATED ELEMENT IN THE LIST: ')

if occur == 'y':
    print(dupe_dict)
else:
    pass
