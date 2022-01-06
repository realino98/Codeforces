input = input()
unique = 0

input = list(input)
char = []
char.append(input[0])
for i in input:
    if i not in char:
        char.append(i)
# print(char)
# # print(unique)
# print(len(char))
if len(char)%2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")