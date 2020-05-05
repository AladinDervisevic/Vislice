for i in range(2, 201):
    if i == 2:
        print(i)
    elif i % 2 != 0:
        d = 3
        while d ** 2 <= i:
            if i % d == 0:
                pass
            d += 2
        print(i)