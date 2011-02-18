# Pollard's rho

import random
from totient import gcd

def pollards_rho(a):
    def stepping(x, n):
        return (x*x+3) % n
    # Factors an integer a
    b = random.randint(1, (a-3))
    print "b is"
    print b
    s = random.randint(0, (a-1))
    print "s is"
    print s
    A = s
    B = s
    g = 1
    
    while g == 1:
        A = stepping(A, b)
        B = stepping(stepping(B, b), b)
        g = gcd(A - B, a)
    if g < a:
        return g
    else:
        return None
        
# tests
if __name__ == "__main__":
    print pollards_rho(2262599)
    