input1 = input()

vowels = ["a", "i", "u", "e", "o", "y", "A", "I", "U", "E", "O", "Y"]

if input1.isalpha():
    if 1 < len(input1) and len(input1) <= 100:
        for vowel in vowels:
            if vowel in input1:
                input1 = input1.replace(vowel, "")
                
        print(input1)
        for char in input1:
            print(char, end=" ")
        print()
        for char in input1:
            # if char not in "".join(vowels):
            input1.replace(char, "."+char)
                
print(input1)