with open("day1.txt") as file:
    lines = file.read().splitlines()
a=0
sum=0
T=[]
for line in lines:
    for char in line:
        if char.isdigit():
            T.append(char)
    a=int(T[0])*10+int(T[-1])
    sum+=a
    T=[]
print(sum)