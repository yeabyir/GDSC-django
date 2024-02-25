print("Palindrome\n")
word = input("Please enter a word: ")

if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
    print(f"because {word[::-1]} is not equal to {word} ")
