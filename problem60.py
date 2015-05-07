"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any
order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
criteria:
-lowest sum
-two concatenate = prime
"""
import itertools

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


def valid_five(a, b, c, d, e, lop):
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)
    list.append(e)
    for i in itertools.permutations(list, 2):
        num = str(i[0])+str(i[1])
        if int(num) not in lop:
            return False
    return True

minimum = 30000

lop = list(list_prime(10**3))

for j in itertools.permutations(lop, 5):
    if valid_five(j[0], j[1], j[2], j[3], j[4], lop) and j[0]+j[1]+j[2]+j[3]+j[4] < minimum:
        print(j[0], j[1], j[2], j[3], j[4], minimum)

