char_input = input("Enter a character: ")
vowels = ["a", "e", "i", "o", "u"]
if char_input.lower() in vowels:
    print("Vowels are not allowed in the input")
elif len(char_input) > 1:
    print("The length of the character should be 1") 
else:   
    for i in range(1, 10):
        if i % 2 == 1:
            print(char_input * (i - 1) + char_input)

            
