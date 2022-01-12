s = input().split()
n = int(s[0])
k = int(s[1])

if 2 <= n <= 10**9 and 1 <= k <= 50:
    for i in range(k):
        if n%10 == 0:
            n /= 10
        elif n%10 >0:
            n -= 1
print(int(n))
