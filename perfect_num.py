num=int(input("enter a number"))
sum=0
num1=num
for i in range(1,num):
    if num%i==0:
        sum=sum+i

if num1==sum:
    print(f"the number {num1} is perfect number ")
else:
    print("the number is not perfect number")