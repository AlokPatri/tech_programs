def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result
string=input("Enter a string:")
print(f"Ther string after removing vowels is: {remove_vowels(string)}")

