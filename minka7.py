def flatten(old_list, depth):
    new_list = []
    for i in range(len(old_list)):
        if type(old_list[i])!=type(new_list):
            new_list.append(old_list[i])
        else:
            if 0<depth:
                new_list += flatten(old_list[i], depth-1)
            else:
                new_list.append(old_list[i])
    return new_list
for i in range(8):
    print(flatten([1, 2, [3, 4, [5, 6], [[7, 7.5, [7.8, [7.9,[[7.99]]]]]], 8, 9], 10], i))
