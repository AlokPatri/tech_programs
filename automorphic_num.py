# an number is automorphic number is a number whose square ends with the same digits as the number itself
num=int(input("enter a number"))
num_sqr=num*num
divisor=1
while num_sqr!=0:
    digit=num_sqr%(10^divisor)
    divisor=divisor+1
    k=0
    if digit==num:
        print(f"the number {num} is automorphic number")
        k=k+1
        break
    else:
        continue
if k==0:
    print("the number is not automorphic number")