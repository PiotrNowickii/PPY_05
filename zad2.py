import math


def prime(*n):
    for x in n:
        if x == 1 or x == 0:
            print(str(x) + " is not prime")
            continue
        tmp = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if (x % i) == 0:
                tmp = False
                break
        if tmp:
            print(str(x) + " is prime")
        else:
            print(str(x) + " is not prime")


prime(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 19)
