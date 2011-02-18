# Brute Force Factorization

import math

def bff(n):
    """
    Try and find factors of a number using brute force (simple)
    """
    start_c = 2
    factors = []
    while n != 1:
        if (n % start_c) == 0:
            factors.append(start_c)
            n = n / start_c
            start_c += 1
        else:
            start_c += 1
            
    return factors
    
def fermat_diff_sq(a):
    """
    Calculate x^2 and y^2 so that (x+y)(x-y) = x^2 - y^2 = a.
    """
    x = math.ceil(math.sqrt(a))
    t = 2*x + 1
    d = math.pow(x,2) - a # different before our current estimate of x^2 and a, or y^2 upon correct difference of the squares
    while(int(math.sqrt(d)) != math.sqrt(d)): # test if d is a square 
        d = d + t
        t = t + 2
    x = math.sqrt((d+a))
    y = math.sqrt(d)
    return ((x+y), (x-y))
    
# tests
if __name__ == '__main__':
    #print bff(2431)
    #print bff(32442134)
    print fermat_diff_sq(88)