from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonocci(n):
  ''' Formula: (n-1) + (n-2) ''' 
    if type(n) != int:
        raise ValueError("Nth term, Must be a positive integer") 
    if n < 1:
        raise ValueError("Nth term, Must be a positive integer")    
    if n == 1:
        return 1
    elif n==2:
        return 1
    elif n > 2:
        return (n-1) + (n-2)
for n in range(1,10):
    print("Fibonacci Series: ", n, ":", fibonocci(n))