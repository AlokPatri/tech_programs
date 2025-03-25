def remove_all_char_except_alphabet(s):
    all_alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in s:
        if char not in all_alphabet:
            s=s.replace(char,"")
    return s
string=input("Enter a string:")
print("the string after removing all characters except alphabet is:",remove_all_char_except_alphabet(string))

            
        