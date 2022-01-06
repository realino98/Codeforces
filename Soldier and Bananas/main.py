#k n w
#dollars, has n dollars, amount of bananas
#ik
input1 = input().split()
k = int(input1[0])
n = int(input1[1])
w = int(input1[2])
total = 0
for i in range(w):
    total += k*(i+1)

if total>n:
    print(total-n)
else:
    print(0)

