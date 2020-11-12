


# открываем - что-то делает с ним - закрываем

# запись в файл
with open("hello.txt", "w") as file1:
    file1.write("hello world")
    file1.write("\n good bye")


with open("hello.txt", "w") as file1:
        file1.write("hello world")


# прочитать и записать к себе в код

with open("27-A_demo.txt", "r") as file:
    f = file.read()
    print(f)