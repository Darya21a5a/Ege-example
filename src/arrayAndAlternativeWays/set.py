# set ==> множества, то есть только УНИКАЛЬНЫЕ ЗНАЧЕНИЯ
# не дает гарантии на порядок значений

# создание
s = {"Cat", "Dog", "Mouse", "Sneak", "Cat", "Dog"}
print(s)

# добавить

s.add("Elephant")
print("Add = ", s)

# удалить
s.remove("Mouse")
print("Remove = ", s)

# s.clear()

# объединить

#s.update()
#s.union()

# перебор
for i in s:
    print(i)
# другие

len(s)
