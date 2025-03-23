num=int(input("enter any number"))
#findig sum of digit of number
sum=0
num1=num
while num!=0:
    digit=num%10
    sum+=digit
    num=num//10
print(f"sum of digit {num1}",sum)