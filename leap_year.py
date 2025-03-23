year=int(input("enter any year"))
# to checking the year is lear year or not
# a leap year is a year that is divisible by 4 
# but if it is divisible by 100 then it must be divisible by 400 to be a leap year
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("this is leap year")
        else:
            print("not a leap year")
    else:s
        print("leap year")
else:
    print('not leap year')