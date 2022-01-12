input1 = input()
a = int(input1.split()[0])
b = int(input1.split()[1])
years = 0
#every year a*3
#every year b*2
if 1 <= a and a <= b and b <= 10:
    while a <= b:
        a = a*3
        b = b*2
        years += 1

print(years)