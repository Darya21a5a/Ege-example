a = 2
b = 3


print("a > b = ", a > b)
print("a < b = ", a < b)
# сравнение равны или нет, тут ты поддерждаешь, что они равны
print("a == b = ", a == b)
# сравнение равны или нет, тут ты поддерждаешь, что они неравны
print("a != b = ", a != b)
print("a <= b = ", a <= b)
print("a >= b = ", a >= b)

# if

if (a < b):
    print("It's OK...")
elif (a == b):
    print("Middle mood...")
else:
    print("So bad...")

# логические знаки and or ! not

w1 = 1
w2 = 2
q3 = 6
q4 = 5

if(w1 < w2 and q3 > q4):
    print("Hi")
else:
    print("Hello")
