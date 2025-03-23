def occurance_fo_digit(n,digit):
    count=0
    while n>0:
        reaminder=n%10
        if reaminder==digit:
            count+=1
    return count

num=int(input("enter a number"))
digit=int(input("enter a digit"))
print(f"occurance og digit {digit} is", occurance_fo_digit(num,occurance_fo_digit))