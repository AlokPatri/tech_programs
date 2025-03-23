'''
if there are n people and r available seats, the number of ways they can occupy the seats is given by the permutation formul

P(n,r)=n!/(n-r)!

'''
import math 
def permutation(n,r):
    return math.factorial(n)/math.factorial(n-r)
n=int(input("enter number of people "))
r=int(input*("enter the number of seats "))
if r>n:
    print("seats can not be more then people ")
else:
    print(f"number of ways to seat {n} people in {r} seats {permutation(n,r)}")
    