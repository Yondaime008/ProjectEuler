"""
every odd composite number can be written as a prime + 2*n**2, n is a random number
We need to find the smallest odd composite number that proves this wrong.
"""


def is_prime(n):
   a = [True] * n
   a[0] = a[1] = False
   for (i, isprime) in enumerate(a):
       if isprime:
           yield i
           for n in range(i*i, n, i):
               a[n] = False


def list_odd_composite(n, m):
    for i in range(n, m):
        if i % 2 == 1 and not is_prime(i):
            yield(i)


def list_primes(n):
    for i in is_prime(n):
        yield i


def list_squares(n, m):
    for i in range(n, m):
        yield i**2


def is_goldbach(n, m, l):
    for i in n:
        for j in l:
            if m == 2 * i + j:
                return True
    return False

list_of_primes = list(list_primes(10**4))
list_of_squares = list(list_squares(1, 10**4))
list_odd_composite = list(list_odd_composite(1, 10**4))

print(is_goldbach(list_of_squares, 5777, list_of_primes))

for i in range(1, 10**4):
    if not is_goldbach(list_of_squares, i, list_of_primes):
        print("FOUND", i)

