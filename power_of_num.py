num=int(input("enter the base number"))
power=int(input("enter the power of base number"))
result=1
for i in range(1,power+1):
    result*=num

print(f"the power of {num} to {power} is ",result)