numRows = input('번호')
out=[]
lis=[]
for i in range(1, int(numRows)+1):
    lis.append(1)
    for j in range(0,i):
        out.append(lis)
print(out)
        

    #      1
    #     1 1
    #    1 3 1
    #   1 4 4 1
    #  1 5 8 5 1
