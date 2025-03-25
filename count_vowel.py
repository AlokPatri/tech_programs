def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count
string=input("Enter a string:")
print(f"The number of vowels in the string is: {count_vowels(string)}")
