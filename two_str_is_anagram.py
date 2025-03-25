def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(f"Are '{str1}' and '{str2}' anagrams? {check_anagram(str1, str2)}")




