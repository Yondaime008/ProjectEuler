import itertools
import math


def count_number(n):
    for count in itertools.product(range(3), repeat=10):
        if sum(count) != 10:
            continue
        if sum([i * count[i] for i in range(10)]) == n:
            yield(count)


def valid_odd_sum():
    for i in range(-5, 6):
        if i % 2 == 0:
            yield i*11/2+45


somme_odd = 0
somme_zero = 0
for i in valid_odd_sum():
    i_even = 90 - i
    for j in count_number(i):
        somme_occ = 1
        if j[0] != 0:
            somme_zero += math.factorial(9)*math.factorial(10)
        for k in j:
            if k == 2:
                somme_occ *= k
        somme_odd += math.factorial(10)/somme_occ
print(somme_odd**2-somme_zero)