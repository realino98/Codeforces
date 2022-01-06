stringinput = input()
if len(stringinput) <= 100:
    for i in range(len(stringinput)):
        for number in range(0,len(stringinput)-1,2):
            if int(stringinput[number]) >= int(stringinput[number+2]):
                # print(">")
                stringinput = list(stringinput)
                temp = stringinput[number]
                stringinput[number] = stringinput[number+2]
                stringinput[number+2] = temp
        
print("".join(stringinput))