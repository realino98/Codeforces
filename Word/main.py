s = input()
new_s = list(s)

def check(input):
    up = 0
    low = 0
    for char in input:
        if char.isupper():
            up +=1
        else:
            low +=1
    if up > low:
        print(s.upper())
    if up <= low:
        print(s.lower())
check(new_s)