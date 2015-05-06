"""Finding the prime number under 1000 that is written as sum of the consecutive prime numbers"""
import time


def is_prime(n):
    '''
    check if integer n is a prime, return True or False
    '''
    # 2 is the only even prime
    if n == 2:
        return True
    # integers less than 2 and even numbers other than 2 are not prime
    if n < 2:
        return False
    if not n & 1:  # even numbers
        return False
    # loop looks at odd numbers 3, 5, 7, ... to sqrt(n)
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
tic = time.clock()
i = 2
somme = 0
while somme < 1000000:
    if is_prime(i):
        somme += i
        print(i, somme)
    i += 1
print(somme)
toc = time.clock()
print('time elapsed ', toc-tic)