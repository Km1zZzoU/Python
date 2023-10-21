def flatten(old_list):
    new_list = []
    for i in range(len(old_list)):
        if type(old_list[i])!=type(new_list):
            new_list.append(old_list[i])
        else:
            new_list += flatten(old_list[i])
    return new_list
print(flatten([1, 2, [3, 4, [5, 6], [[7], 8, 9], 10]]))
