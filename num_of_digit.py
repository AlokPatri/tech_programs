def no_of_digit(n):
    count_digit=0
    while n>0:
        digit=n%10
        count_digit+=1
        n=n//10
    return count_digit
num=int(input("enter an integer number"))
print(f"the number of digit",no_of_digit(num))