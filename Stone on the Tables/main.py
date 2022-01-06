input1 = input()
input2 = input()

input1 = int(input1)
output = 0
if len(input2) == input1:
    for a in range(input1):
        try:
            if input2[a] == input2[a+1]:
                output+=1
        except:
            pass
print(output)