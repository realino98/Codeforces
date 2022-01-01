x = 0
n = int(input())
statements = []
if 1 <= n and n <= 150:
    for a in range(n):
        statement = input()
        if len(statement) <= 3:
            if "++X" in statement or "X++" in statement or "--X" in statement or "X--" in statement:
                statements.append(statement)

for i in statements:
    if i == "X++":
        x+=1
    if i == "++X":
        x+=1
    if i == "X--":
        x-=1
    if i == "--X":
        x-=1

print(x)