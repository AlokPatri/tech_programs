num=int(input("enter a number"))
reverse=0
num1=num
while num!=0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

if num1==reverse:
    print(f"the number {num1} is palindrome number")
else:
    print(f"the number {num1} is not palindrome number")