def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

# Example usage
char = input("Enter a character: ")
if is_vowel(char):
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")