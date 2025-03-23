def check_leap(year):
    if(year % 4 ==0 and year % 100!=0) or (year%400==0):
        return True
    return False
def day_in_month(month,year):
    days_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2 and check_leap(year):
        return 29
    return days_month[month]

month=int(input("enter month (1-12)"))
year=int(input("enter year"))

if 1 <= month <= 12:
    print(f" number of days ",{day_in_month(month,year)})