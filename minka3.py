string = input()
mtrx = []
mtrxSTR = []

for i in range(len(string.split('|'))):
    print(string.split('|'))
    for j in range(len(string.split('|')[i].split())):
        print(string.split('|')[i].split())
        mtrxSTR.append(float(string.split('|')[i].split()[j]))
        print(mtrxSTR)
    mtrx.append(mtrxSTR)
    print(mtrx)
    mtrxSTR = []

'''for i in range(len(string.split())):
    if string.split()[i]!='|':
        mtrxSTR.append(float(string.split()[i]))
    else:
        mtrx.append(mtrxSTR)
        mtrxSTR = []'''

indexs = '0 1'
print(mtrx)
print(mtrx[int(indexs.split()[0])][int(indexs.split()[1])])

