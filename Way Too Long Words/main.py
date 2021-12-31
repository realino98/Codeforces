number_of_string = int(input())
strings = []
if number_of_string >= 1 and number_of_string <= 100:
    for n in range(number_of_string):
        new_string = input()
        if len(new_string) > 10:
            new_string = str(new_string[0] + str(len(new_string)-2)+ new_string[len(new_string)-1])
        strings.append(new_string)

for string in strings:
    print(string)

    