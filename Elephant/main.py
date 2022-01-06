import math
x = input()
x = int(x)

if 1 <= x <= 10**6:
    if x <= 5:
        print(1)
    else:
        if(x%5) == 0:
            print(math.floor(x/5))
        else:
            print(math.floor(x/5)+1)
    