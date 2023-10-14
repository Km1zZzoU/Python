def MyZip(arr1, arr2):
    arr = []
    for i in range (min(len(arr1), len(arr2))):
        arr.append((arr1[i], arr2[i]))
    return(arr)

arr1 = [1, 2, 3, 4, 5]
arr2 = ['a', 'b', 'c', 'd']
print(MyZip(arr1, arr2))
