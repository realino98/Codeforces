input1 = input()
input2 = input()

# total1 = int(input1)
input1 = input1
input2 = input2
input_list = [input1, input2]
if 1 <= len(input1) and len(input1) <= 100:
    if 1 <= len(input2) and len(input2) <= 100:
        input_list.sort()
        if input1.lower() == input2.lower():
            print(0)
        elif input_list[0] == input1.lower():
            print(-1)
        elif input_list[1] == input1.lower():
            print(1)

