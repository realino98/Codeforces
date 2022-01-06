input1 = input()
n = int(input1)
numbers = []
for i in range(n):
    input2 = input().split()
    x = int(input2[0])
    y = int(input2[1])
    z = int(input2[2])
    if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
        numbers.append(input2)
total_x = 0
total_y = 0
total_z = 0        
for i in range(n):
    total_x += int(numbers[i][0])
    total_y += int(numbers[i][1])
    total_z += int(numbers[i][2])
# print(total_x, total_y, total_z)
if total_x == 0 and total_y == 0 and total_z == 0:
    print("YES")
else:
    print("NO")