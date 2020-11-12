try:
    file = open("hello.txt", "w")
    try:
        file.write("hello world")
    except Exception as e:
        print(e)
    finally:
        file.close()
except Exception as ex:
    print(ex)

# try - finally
# try - except
# try - except - finally

with open("hello.txt", "w") as file1:
    file1.write("hello world")


