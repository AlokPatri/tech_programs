'''
there are n people in a room the maximum number of handshake that can occur is when evry person shakes hand with every other person exaclty
once
the formula to calculate this is:
handshake=n(n-1)/2

where 
n(n-1) is counts all possible pairs ( since each person can shake hands with n-1 others)
divide by 2 because a handshake hetween A and b is the same as B and A

'''
def max_hand_shake(n):
    return (n*(n-1))//2

n=int(input("enter number of people "))
print("maximum number of handshake",max_hand_shake(n))
