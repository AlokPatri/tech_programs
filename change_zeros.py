def zero_to_one(n):
    result=0
    place=1
    while n>0:
        digit=n%10
        if digit==0:
            digit=1
        result+=digit*place
        place*=10
        n//=10
    return result

print(zero_to_one(1020))