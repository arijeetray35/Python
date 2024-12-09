#code to add two list

a=[[1,2,3],[4,5,6],[7,8,9]]
b= [[3,2,1],[6,5,4],[9,8,7]]
sum= [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for  j in range(0,3):
        sum[i][j]= a[i][j]+b[i][j]
print(sum)
