nth_term=int(input("enter value of nth"))
x1=0
x2=1
k=1
while nth_term!=k:
    s=x1+x2
    x1=x2
    x2=s
    k+=1
print(f"the {nth_term} term is ", x1)
    