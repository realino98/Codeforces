input1 = input().split()
n = input1[0]
k = input1[1]
n = int(n)
k = int(k)
input2 = input().split()
passed = 0
if 1 <= k and k <= n and n <= 50:
    for a in input2:
        if 0 <= int(input2[input2.index(a)]) and int(input2[input2.index(a)]) <= 100:
            if int(input2[input2.index(a)]) >= int(input2[input2.index(a) + 1]):
                if len(input2) == n:
                    # print(int(a))
                    if int(a) > k:
                        passed += 1
                    if int(a) == 1:
                        passed += 1
print(passed)