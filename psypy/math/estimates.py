# Some estimation functions

import math

def approx_primes(a):
    # Approximate number of primes for a
    return a / math.log(a)
    
def approx_bits(a):
    # Approxiate lower bound of bits for a
    return math.log(a, 2)
    