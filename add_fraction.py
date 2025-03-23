def gcd(a,b):
    while b:
        a,b=b, a%b
    return a
def add_fraction(a,b,c,d):
    num=a*d + b*c
    deno=b*d
    g=gcd(num,deno)
    return num//g, deno//g
print(add_fraction(1,2,1,3))