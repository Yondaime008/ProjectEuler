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
import time

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
    for i in itertools.combinations(list, 2):
        num = str(i[0])+str(i[1])
        num_inv = str(i[1])+ str(i[0])
        if int(num) not in lop or int(num_inv) not in lop:
            return False
    return True


def valid_four(a, b, c, d, lop):
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)
    for i in itertools.combinations(list, 2):
        num = str(i[0])+str(i[1])
        num_inv = str(i[1])+ str(i[0])

        if int(num) not in lop or int(num_inv) not in lop:
            return False
    return True


def valid_three(a, b, c, lop):
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    for i in itertools.combinations(list, 2):
        num = str(i[0])+str(i[1])
        num_inv = str(i[1])+ str(i[0])
        if int(num) not in lop or int(num_inv) not in lop:
            return False
    return True


def valid_two(a, b, lop):
    list = []
    list.append(a)
    list.append(b)
    for i in itertools.combinations(list, 2):
        num = str(i[0])+str(i[1])
        num_inv = str(i[1])+ str(i[0])
        if int(num) not in lop or int(num_inv) not in lop:
            return False
    return True

tic = time.clock()

minimum = 30000

lop = list(list_prime(10**4))
lop1 = list(list_prime(10**6))
lop.remove(2)
lop.remove(5)


def find_next_element_two(i, list1, list2):
    for b in list1:
        if valid_two(i, b, list2):
            yield b

for a in lop:
    next_elements_two = list(find_next_element_two(a, lop, lop1))
    for b in next_elements_two:
        if b != a:
            for c in next_elements_two:
                if c != a and c != b and valid_three(a, b, c, lop1):
                    for d in next_elements_two:
                        if d != a and d != b and d != c and valid_four(a, b, c, d, lop1):
                            print(a, b, c, d)
                            for e in next_elements_two:
                                if e != a and e != b and e != c and e != d and a+b+c+d+e < minimum and valid_five(a, b, c, d, e, lop1):
                                    minimum = a+b+c+d+e
                                    print(a, b, c, d, e, minimum)
                                else:
                                    next_elements_two.remove(e)
                        else:
                            next_elements_two.remove(d)
                else:
                    next_elements_two.remove(c)
    lop.remove(a)

toc = time.clock()
print("Found", a, b, c, d, e, "in", toc-tic, "s")
