num= int(input("enter the num"))
fact_list=[]
for i in range(1,num//2+1):
    if num%i==0:
        fact_list.append(i)
    
print(f"the factors of {num} are ",fact_list)