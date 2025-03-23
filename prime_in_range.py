start_point=int(input("enter the start point "))
end_point=int(input("enter the end point of range"))
for i in range(start_point,end_point+1):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k+=1
    if k==2:
        print("prime number",i)
    else:
        print("not prime number",i)