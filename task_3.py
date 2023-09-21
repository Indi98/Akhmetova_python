mas=[]
k=input().split()
for i in k:
    mas.append(int(i))


for j in range(len(mas)):
    if mas[j]%3==0:
        print(mas[j])