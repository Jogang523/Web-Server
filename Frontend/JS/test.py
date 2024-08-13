numRows = input('번호')
out=[]
lis=[]
for i in range(1, int(numRows)+1):
    lis.append(i)
    out.append(lis[0:2])
print(out)