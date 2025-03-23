num=int(input("enter a number"))
#to check the given number is perfect square or not without using built in function
#A number is a ferfecct square if and only if the sum of the first odd numbers equals N.
#1=1^2
# 1+3=4=2^2
#1+3+5=9=3^2
#1+3+5+7=16=4^2

# this means that if you keep subtracting consecutive odd numbers from n and reach zero, 
#the n is a perfect number
odd=1
num1=num
while num>0:
    num=num-odd
    odd=odd+2

if num==0:
    print(f"given number {num1} is a perfect number")
else:
    print(f"given number {num1} is not a perfect number")