with open("day1.txt") as file:
    lines = file.read().splitlines()
a=0
sum=0
T=[]
for line in lines:
    line = line.replace('one', "o1e")
    line = line.replace('two', "t2o")
    line = line.replace('three', "f3e")
    line = line.replace('four', "f4r")
    line = line.replace('five', "f5e")
    line = line.replace('six', "s6x")
    line = line.replace('seven', "s7n")
    line = line.replace('eight', "e8t")
    line = line.replace('nine',"n9e")
    for char in line:
        if char.isdigit():
            T.append(char)
    a = int(T[0]) * 10 + int(T[-1])
    sum += a
    T = []
print(sum)

