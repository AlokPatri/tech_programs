def is_alphabet(char):
    # Check if the character is an uppercase letter
    if 'A' <= char <= 'Z':
        return True
    # Check if the character is a lowercase letter
    elif 'a' <= char <= 'z':
        return True
    else:
        return False

# Test the function
char = input("Enter a character: ")
if is_alphabet(char):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")    
