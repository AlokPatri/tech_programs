num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the thirsd number"))
great1=num if num1>num2 else num2
greatest=great1 if great1>num3 else num3
print("the greatest number in three number", greatest)