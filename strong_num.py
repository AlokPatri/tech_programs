num=int(input("enter the number"))
fact_sum=0
num1=num
while num!=0:
    digit=num%10
    fact_factorial=1
    for j in range(1,digit+1):
        fact_factorial=fact_factorial*j
    num=num//10
    fact_sum=fact_sum+fact_factorial

if num1==fact_sum:
    print(f"the number is {num1} is storng number")
else:
    print("the number is not strong number")
