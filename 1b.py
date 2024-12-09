#python code to create a user defined sublist of  3
n = int(input("enter  number of sublist:"))
l=[]
for i in range(1,n+1):
    l.append([])
print(l)

for i in range(0,len(l)):
    k=int(input(f"enter number of elements in sublist{i+1}: "))
    for j in range(0,len(l)):
        k=int(input(f"enter the sublist elements{i+1}: "))
        l[i].append(k)
print(l)
