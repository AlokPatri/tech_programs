num1=int(input("enter first number"))
num2=int(input("enter second number"))
lcm=1
k=2
num11=num1
num22=num2
while num1>1 or num2>1:
    if num1%k==0 and num2%k==0:
        lcm=lcm*k
        num1=num1//k
        num2=num2//k
    elif num1%k==0:
        lcm=lcm*k
        num1=num1//k
    elif num2%k==0:
        lcm=lcm*k
        num2=num2//k
    else:
        k=k+1

print(f"the lcm of {num11} and {num22} is {lcm} ")

# we know that 
#LCM * HCF = product of numbers(first number * second number)
"""
import math
def find_lcm(a,b):
return abs(a*b)//math.gcd(a,b) # lcm formula

num1=int(input("enter the frist number))
num2=int(input("enter the seocndo nukbr))
lcm=find_lcm(num1,num2)
print(lcm)

"""
# program for more than two numbers 

'''
import math
from functools import reduce

def find_lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

def lcm_multiple(*numbers):
    return reduce(find_lcm,numbers)

nums=list(map(int, input("enter numbers separated by space: ").split()))
lcm=lcm_multiple(*nums)
print(lcm)
'''