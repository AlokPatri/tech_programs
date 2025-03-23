while True:
    try:
        num=int(input("enter the end point of natural number"))
        #now we can calculate sum of natural number using this formula sum=n(n+1)/2
        sum=num*(num+1)/2
        print(f"the sum of {num} natural numbers=",sum)
        break
    except ValueError:
        print("invalid input! please enter a valid range")
