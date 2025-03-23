import math
from functools import reduce
'''def hcf(*arg):
    min_num=min(arg)
    result=1
    k=1
    while k<=min_num:
        if arg%k==0:
            result=result*i
        else:
             k=k+1
    return result
print(hcf(4,8,12))'''

def get_hcf(*num):
    return reduce(math.gcd,num)

num_list=list(map(int,input("enter numbers separated by spases").split()))
hcf=get_hcf(*num_list)
print(f"the HCF of {num_list} is {hcf}")