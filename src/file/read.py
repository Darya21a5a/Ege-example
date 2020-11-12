# readline() одна строка
# read() все строки
# readlines() все строки перекидываются в лист

list1 = open("27-A_demo.txt", "r").read().split(" ")

for i in list1:
    if len(i) == 0:
        list1.remove(i)

list2 = []
for i in list1:
    if i.__contains__("\n"):
        list2.append(i.replace("\n", " ").split(" "))

list3 = []
for i in list2:
    if len(i) > 1:
        for j in i:
            list3.append(j)
            if len(j) == 0:
                list3.remove(j)

print(list3)
