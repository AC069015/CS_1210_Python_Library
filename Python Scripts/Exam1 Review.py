def bar(a, b, c):
    a = 7 - b
    c[0] = a + 15
    c = [8]
    return [a, b, c]

def foo():
    a = 4
    b = a
    c = [1, 2, b]
    temp = bar(a, b, c)
    a = a + 1
    return (a, b, c, temp)

def problem2a():
    w = 1
    x = 17
    y = w + 1
    z = [x, y]
    y = y + w
    z[0] = x + 1
    z.append(y)
    print(w, x, y, z)

def problem2b():
    x = 12
    y = 3
    z = 5
    if ((y > z) or (z < x)):
        print("EK")
        if (x < 10):
            print("DO")
        elif (z < 10):
            print("TEEN")
        print("CHAAR")
    else:
        if (x < 20):
            print("PAANCH")
        else:
            print("CHAH")
        print("SAAT")
    if ((z-y) > 0):
        print("AATH")


