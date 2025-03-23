while True:
    try:
        num1=int(input("enter first number"))
        break
    except ValueError:
        print("enter valid input")
while True:
    try:
        num2=int(input("enter second number"))
        break
    except ValueError:
        print("enter the valid input")
greatest_num=num1 if num1>num2 else num2
print("the greatest number is ",greatest_num)