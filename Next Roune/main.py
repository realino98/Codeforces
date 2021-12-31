finput = input().split()
n = int(finput[0])
k = int(finput[1])
a = input().split()
passed = 0
flag = []
check = False
if n >= k:
    if n == len(a):
        for x in a:
            if int(a[a.index(x)]) >= int(a[a.index(x)+1]):
                flag.append(True)
            else:
                flag.append(False)
        # print(flag)
        if False in flag:
            check = False
        else:
            check = True

        for score in a:
            if int(score) > k and check:
                passed += 1
        print(passed)