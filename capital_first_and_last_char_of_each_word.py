def capital_first_and_last_char_of_each_word(s):
    list_of_words = s.split() # split the string into a list of words
    result = []
    for word in list_of_words:
        if len(word) < 2: # if the word has less than 2 characters only one character is present
            result.append(word.upper())
        else:
            result.append(word[0].upper() + word[1:-1] + word[-1].upper())
    return ' '.join(result)
string=input("Enter a string: ")
print(f"the frist and last char capital string",capital_first_and_last_char_of_each_word(string))
