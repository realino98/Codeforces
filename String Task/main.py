input1 = input()

vowels = ["a", "i", "u", "e", "o", "y", "A", "I", "U", "E", "O", "Y"]
if input1.isalpha():
    if 1 < len(input1) and len(input1) <= 100:
        for vowel in vowels:
            input1 = input1.replace(vowel, "")

        for char in input1:
            if char != ".":
                input1 = input1.replace(char, "."+char)
        input1 = input1.replace("..", ".")
                # print(True)
        input1 = str(input1)
print(input1)