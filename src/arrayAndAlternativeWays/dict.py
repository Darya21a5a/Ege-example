# English dictionary => английский словарь
# agree(key) == согласиться(value)
# {key - value, key - value, key - value}

# создание словаря
englishDict = {"Agree": "Согласиться", "Bad": "Плохо"}
print(englishDict)

# получение по ключу
print("Get = ", englishDict.get("Agree"))

# удаление по ключу
englishDict.pop("Agree")
print("Remove = ", englishDict)

# полная очистка словаря
# englishDict.clear()
# print(englishDict)

# вставка нового словаря
englishDict2 = {"Suggest": "Предлагать", "Cat": "Кот"}
englishDict.update(englishDict2)
print("Update = ", englishDict)

# перебор по ключам
for key in englishDict.keys():
    print("Key = ", key)

# перебор по значениям
for value in englishDict.values():
    print("Value = ", value)