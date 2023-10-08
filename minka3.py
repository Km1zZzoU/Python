string = input()
mtrx = []
mtrxSTR = []
for i in range(len(string.split())):
    if string.split()[i]!='|':
        mtrxSTR.append(float(string.split()[i]))
    else:
        mtrx.append(mtrxSTR)
        mtrxSTR = []
mtrx.append(mtrxSTR)
indexs = input()
print(mtrx[int(indexs.split()[0])][int(indexs.split()[1])])
    

