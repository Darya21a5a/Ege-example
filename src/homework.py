def f(x, deg):
    i = 0
    sum = x % 10

    while x != 0:
        i += 1
        x //= 10
        sum += x % 10
    sum /= i
    sum **= deg
    return sum


a = int(input())
b = int(input())

if (f(a, b) > (10 ** 7)):
    while (a > (10 ** 7)):
        a //= 10
    print('it is better way = ', ' ', int(a), '...')
else:
    i = 0
    while (a < (10 ** 9)):
        a *= 10
        i += 1
        a += i
        print('it is better way = ', ' ', int(a), '...')

a = f(a, b)

print(int(a))
