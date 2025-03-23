def deci_to_oct(n):
    oct_num=""
    if n==0:
        return 0
    while n>0:
        remainder=n%8
        oct_num=str(remainder)+oct_num
        n=n//8
    return oct_num
deci_num=int(input("enter a decimal number:"))
print("octal", deci_to_oct(deci_num))