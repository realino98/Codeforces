query = int(input())
array = []
for q in range(query):
    if 1 <= q and q <= 5*10**5:
        input1 = input().split()
        mode = int(input1[0])
        x = int(input1[1])
        y = int(input1[2])
        if 1 <= x and x <= 5*10**5 and 1 <= y and y <= 5*10**5:
            if mode == 1:
                array.append(x)
            if mode == 2:
                for a in array:
                    if a == x:
                        array[array.index(a)] = y
        
print(array)