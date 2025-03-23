num=int(input("enter the number"))
prime_fact=[]
for i in range(1,num//2+1):
    if num%i==0:
        k=0
        for j in range(1,i+1):
            if i%j==0:
                k=k+1
        if k==2:
            prime_fact.append(i)

print(f"the prime factors of number {num} are", prime_fact)