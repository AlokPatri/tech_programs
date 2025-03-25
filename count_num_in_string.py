def count_num_in_string(string):
    count=0
    num="0123456789"
    for i in string:
        if i.isdigit() or i in num:
            count+=1
    return count
string=input("Enter a string:")
print("The number of digits in the string is:",count_num_in_string(string))
