def gcd(a,b):
   while b:
      a, b = b, a % b
   return a

def totient(n):
    tot, pos = 0, n-1
    while pos>0:
       if gcd(pos,n)==1: tot += 1
       pos -= 1
    return tot
    
if __name__ == '__main__':
    print totient(187)