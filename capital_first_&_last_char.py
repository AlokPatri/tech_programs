def capital_first_and_last_char(s):
    if len(s) < 2:
        return s.upper()
    else:
        return s[0].upper() + s[1:-1] + s[-1].upper()

string=input("Enter a string: ")
print(f"the frist and last char capital string",capital_first_and_last_char(string))