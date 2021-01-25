from sys import stdin, stdout
from decimal import *
import math

def SqrtByAverage(n):
    ''' Avarage method

    '''
    if n < 0:
        return 'n cannot be smaller than 0.'
    if n == 0 or n == 1:
        return n

    EPSILON = 1e-15
    low, high = 0, 0

    if n < 1:
        low = 0
        high = 1
    else:
        low = 1
        high = n
    while high - low > EPSILON:
        mid = (high + low) / 2
        
        if mid*mid > n:
            high = mid
        else:
            low = mid
    
    return low


def SqrtByNewtonMethod(n):
    ''' Newton method: https://en.wikipedia.org/wiki/Newton%27s_method
    
    '''
    if n == 0 or n == 1:
        return n
    
    root = n / 2
    
    for k in range(100000):
        root = (1/2)*(root+(n/root))
    
    return root


if __name__ == '__main__':
    n = int(stdin.readline().strip())
    res_sys = Decimal(math.sqrt(n)) # system method
    res_avg = Decimal(SqrtByAverage(n))
    res_newton = Decimal(SqrtByNewtonMethod(n))
    stdout.writelines('System  Method: %.32f\nAverage Method: %.32f\nNewton  Method: %.32f' % (res_sys, res_avg, res_newton))