file=open("a.txt",'r') 
x=[]
for i in file.readlines():
    for j in i.split():
        x.append(j)
print("unique strings in file",x)

print("unique strings")
x=set(x)
print(*x)