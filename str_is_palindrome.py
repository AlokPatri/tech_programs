def check_palindrome(s):
    reverse_s=s[::-1]
    if s==reverse_s:
        return True
    else:
        return False
string=input("Enter a string:")
if check_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    