input1 = input()
n = int(input1.split()[0])
t = int(input1.split()[1])
input2 = input()
input2 = list(input2)
if 1 <= n <= 50 and 1 <= t <= 50:
    for time in range(t):
        for person in range(n-1):
            #check
            if input2[person] == "B" and input2[person+1] == "G":
                input2[person] = "G"
                input2[person+1] = "B"
        print(input2)
print(input2)