input = input()
zero = 0
one = 0
if len(input) <= 100:
    if "1" not in input or "0" not in input:
        pass
    else:
        input = list(input)
        for i in range(len(input)-1):
            if input[i] == "0" and input[i+1] == "0":
                zero+=1
            elif input[i] == "1" and input[i+1] == "1":
                one+=1
    # print(zero, one)
    if zero > 3 or one > 3:
        print("YES")
    else:
        print("NO")
            
print(input.count("0"))
print(input.count("1"))