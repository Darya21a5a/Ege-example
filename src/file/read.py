# readline() одна строка
# read() все строки
# readlines() все строки перекидываются в лист

list2 = list([])
list3 = open("27-A_demo.txt", "r").read().split(" ")

for i in list3:
    if(len(i) == 0):
        list3.remove(i)

list4 = []
for i in list3:
    if(i.__contains__("\n")):
        k =  i.replace("\n", " ")
        list4.append(k)


list5 = []

for i in list4:
    if(i.__contains__(" ")):
        o = i.split(" ")
        list5.append(o)

list6 = []
for i in list5:
    if(len(i) > 1):
        for j in i:
            list6.append(j)

for i in list6:
    if(len(i) == 0):
        list6.remove(i)

print(list6)