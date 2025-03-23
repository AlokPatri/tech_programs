num=int(input("enter any number"))
k=0
for i in range(1,num+1):
    if num%i==0:
        k+=1
if k==2:
    print("the number is prime number")
else:
    print("the number is not prime number")