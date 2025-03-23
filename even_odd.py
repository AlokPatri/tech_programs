
# checking the number is even of odd

while True:
    try:
        num=int(input("enter a number"))
        if num%2==0:
            print("the number is even")
            break
        else:
            print("number is odd")
            break
    except ValueError:
        print("Invalid input! please enter valid input number")