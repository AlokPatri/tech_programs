# two numbers form a friendly pair if their abundance index is the same
#abundance index=sum of proper divisors/number itself
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
divisor_sum1=0
divisor_sum2=0
for i in range(1,num1):
    if num1%i==0:
        divisor_sum1=divisor_sum1+i

for j in range(1,num2):
    if num2%j==0:
        divisor_sum2=divisor_sum2+j

abund_indx1=divisor_sum1/num1
abund_indx2=divisor_sum2/num2
if abund_indx1==abund_indx2:
    print(f"the given number {num1,num2} is friendly pair")
else:
    print("not friedly")