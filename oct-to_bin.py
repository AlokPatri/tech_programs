def oct_to_bin(oct_num):
    oct_to_bin_map={
        "0":"000","1":"001",
        '2':"010",'3':'011',
        '4':'100','5':'101',
        '6':'110','7':'111'
    }

    bin_num=""
    for digit in str(oct_num):
        bin_num+=oct_to_bin_map[digit]
    return bin_num.lstrip("0")

oct_num=input("enter an octal number")
print("binary is",oct_to_bin(oct_num))