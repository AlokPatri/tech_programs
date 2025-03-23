import math as mt
num=int(input("enter a number"))
# number = sum of digit of number is armstrong number
num1=num
sum=0
no_digit=0
while num!=0:
    digit=num%10
    no_digit=no_digit+1
    num=num//10
num2=num1
while num1!=0:
    digit=num1%10
    sum=sum+mt.pow(digit,no_digit)
    num1=num1//10

if num2==sum:
    print(f"the number {num2} is armstrong number")
else:
    print("the number is not armstrong number")