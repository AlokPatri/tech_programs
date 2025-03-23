def deci_to_bin(n):
    bin_num=""
    if n==0:
        return 0
    while n>0:
        remainder = n%2
        bin_num=str(remainder)+bin_num
        n=n//2
    return bin_num

deci_num=int(input("enter a decimal number:"))
print("binary", deci_to_bin(deci_num))

