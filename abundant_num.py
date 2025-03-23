# A number is abundant if the sum of its proper divisors is greter the number iitself
num=int(input('enter a number '))
divisor_sum=0
num1=num1
for i in range(1,num):
    if num%i==0:
        divisor_sum=divisor_sum+i
    
if num1<divisor_sum:
    print(f"the given numbr {num1} is abundant number")
else:
    print("the numbr is not abundant number")