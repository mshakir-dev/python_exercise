# Prime Number: Only divisible by itself  --- e.g(7)
# Composite Number: Can be factored into smaller integers --- e.g(4 = 2*2)

def is_prime(n):
  """ Return True if n is prime otherwise false """
  # 1 is not prime 
  if n == 1:
    return False
  for d in range(2, n):
    if n % d == 0:
      return False
  return True
print(is_prime(19))

""" Python Unit Test Function: """
# for n in range(1, 21):
#   print(n, "is : ", is_prime_v1(n))