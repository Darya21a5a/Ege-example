i = 1
while(i < 10):
    print(i)
    i += 1

# do - while



q = 1
w = 1
while (q < 10):
    while (w < 10):
        print("w = ", w)
        w+=1
        if (w == 8):
            continue
    q+=1
    print("q = ", q)