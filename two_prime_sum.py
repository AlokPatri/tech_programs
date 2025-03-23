def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def sum_of_two_prime(n):
    for i in range(2,n):
        if is_prime(i) and is_prime(n-i):
            return i, n-i 
    return None
print(sum_of_two_prime(34))