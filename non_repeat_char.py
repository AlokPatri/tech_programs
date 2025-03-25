def not_repeat_char(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char in s:
        if frequency[char] == 1:
            return char
    return None

string=input("Enter a string: ")
print(f"The first non-repeating character in the string is: {not_repeat_char(string)}")
