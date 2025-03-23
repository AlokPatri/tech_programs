# harshad number is known as Niven number
# the Niven number is a number that is divisible by the sum of ist digits.
num=int(input("enter a number"))
num1=num
digit_sum=0
while num!=0:
    digit=num%10
    digit_sum=digit_sum+digit
    num=num//10

if num1%digit_sum==0:
    print(f"the number {num1} is Harshad number")
else:
    print(f"the number {num1} is not Harshad number")
    