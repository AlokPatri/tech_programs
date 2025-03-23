terms=int(input("enter the terms of fibonacci "))
x1,x2=0,1
for i in range(terms):
    print(x1)
    s=x2+x1
    x1=x2
    x2=s