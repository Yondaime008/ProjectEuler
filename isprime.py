__author__ = 'abnasser'
def primes_sieve2(limit):
   a = [True] * limit
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
       if isprime:
           yield i
           for n in range(i*i, limit, i):
               a[n] = False


def isprime(limit):
   a = [True] * limit
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
       if isprime:
           yield i
           for n in range(i*i, limit, i):
               a[n] = False

def list_prime(n):
    isprimelist = isprime(n)
    for i in isprimelist:
        if i:
            yield(i)