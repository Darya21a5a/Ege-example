# массив = это набор данных

# [1,2,3,4,5]
#  0 1 2 3 4

arr = [1, 2, 3, 4, 1, 4]
# добавление вначало
arr.append(6)
print("Append = ", arr)
# вставка
arr.insert(2, 6)
print("Insert = ", arr)

# удаление
# arr.clear() # полное удаление массива/ листа

arr.remove(2)
print("Remove = ", arr)

# другие
print("Contain = ", arr.__contains__(1))
print("Count = ", arr.count(1))
arr.sort()
print("Sort = ", arr)
arr.reverse()
print("Reverse = ", arr)

print("Size = ", len(arr))
print("Min element = ", min(arr))
print("Max element = ", max(arr))

# создать лист
numbers = list(range(-13, 13))
print(numbers)

arr1 = [1, 2, "Hello", 4, 2.2]
print(arr1)


# перебор == цикл

for i in arr1:
    print(i)


# присоединением массивов
q = [1, 2, 4, 5, 1]
w = [4, 3, 5, 7]
# конкантенация => между двумя элементами стоит +, НО ЭТО НЕ СЛОЖЕНИЕ
print(q + w)