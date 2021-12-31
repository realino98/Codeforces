import math
insert = input()
insert = insert.split()

n = int(insert[0])
m = int(insert[1])
a = int(insert[2])

if n >= 1 and n <= 10**9 and m >= 1 and m <= 10**9 and a >= 1 and a <= 10**9:
    print(math.ceil(n/a)*math.ceil(m/a))