import matplotlib.pyplot as plt
import numpy as np
import time

def total_sum(arr):
    total_sum = 0
    for ar in arr:
        for element in ar:
            total_sum += element
    return total_sum


size = 64
nptasya = np.random.randint(2, size  = (size, size))
tasya = []
for i in range(size):
    ar = []
    for j in range(size):
        ar.append(nptasya[i][j])
    tasya.append(ar)

img = plt.imshow(tasya, cmap='binary')
plt.axis('off')
start_t = time.time()
for _ in range(1024):
    new_tasya = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            num = tasya[(i + 1) % size][(j - 1) % size] + tasya[(i + 1) % size][j % size] + tasya[(i + 1) % size][(j + 1) % size] + tasya[i % size][(j - 1) % size] + tasya[i % size][(j + 1) % size] + tasya[(i - 1) % size][(j + 1) % size] + tasya[(i - 1) % size][j % size] + tasya[(i - 1) % size][(j - 1) % size]
            if (tasya[i][j] == 1):
                if num != 2 and num != 3:
                    new_tasya[i][j] = 0
                else:
                    new_tasya[i][j] = tasya[i][j]
            else:
                if num == 3:
                    new_tasya[i][j] = 1
                else:
                    new_tasya[i][j] = tasya[i][j]

    img.set_data(new_tasya)
    tasya = new_tasya
print(time.time() - start_t)
print(total_sum(tasya))

start_t = time.time()
for _ in range(1024):
    new_nptasya = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            num = nptasya[(i + 1) % size][(j - 1) % size] + nptasya[(i + 1) % size][j % size] + nptasya[(i + 1) % size][(j + 1) % size] + nptasya[i % size][(j - 1) % size] + nptasya[i % size][(j + 1) % size] + nptasya[(i - 1) % size][(j + 1) % size] + nptasya[(i - 1) % size][j % size] + nptasya[(i - 1) % size][(j - 1) % size]
            if (nptasya[i][j] == 1):
                if num != 2 and num != 3:
                    new_nptasya[i][j] = 0
                else:
                    new_nptasya[i][j] = nptasya[i][j]
            else:
                if num == 3:
                    new_nptasya[i][j] = 1
                else:
                    new_nptasya[i][j] = nptasya[i][j]

    img.set_data(new_nptasya)
    nptasya = new_nptasya
print(time.time() - start_t)
print(total_sum(nptasya))

plt.show()