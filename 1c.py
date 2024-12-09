
#pytgon code to create multiplication table of nested list
n = int(input("enter  number of sublist:"))
l=[]
for i in range(1,n+1):
    l.append([])
print(l)

for i in range(0,len(l)):
    c=int(input("enter number of elements in sublist: "))
    for j in range(1,4):
        l[i].append(c*j)
print(l)
