def deci_to_hex(n):
    hex_num="0123456789ABCDEF"
    hexa_deci=""
    if n==0:
        return 0
    while n>0:
        remainder=n%16
        hexa_deci=hex_num[remainder]+hexa_deci
        n=n//16
    return hexa_deci

deci_num=int(input("enter a decimal number:"))
print("hexadecimal",deci_to_hex(deci_num))