finput = input().split()
m = int(finput[0])
n = int(finput[1])

if 1 <= m and m <= n and n <= 16:
    print(int(m*n/2))
