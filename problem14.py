import time

"""#which number under 1000000 produces the largest chain
n = n/2 if n%2==0
n=3n+1  else"""


def find_next_element(n):
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    return n


def length_of_chain(n):
    length = 1
    while n != 1:
        n = find_next_element(n)
        length += 1
    return length


def find_max_length(n):
    maximum = 0
    while n < 10**6:
        l = length_of_chain(n)
        if l > maximum:
            maximum = l
            index = n
        n += 1
    print("maximum length reached is", maximum, " for the starting number ", index)
tic = time.clock()
find_max_length(1)
toc = time.clock()
print("Time elapsed :", toc-tic)