input = input()
if len(input) <= 10**3:
    input = list(input)
    # for i in input:
    #     if not input[0].islower():
    #         if input[input.index(i)].isupper():
    #             input[input.index(i)] = str(input[input.index(i)])
    #         else:
    #             print(input[input.index(i)])
    if input[0].islower():
        input[0] = input[0].upper()
print("".join(input))
        