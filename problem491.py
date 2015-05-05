from itertools import *

numbers = '01234567890123456789'


def generate_double_palindrome(string):
    result = 0
    for j in permutations(string, 20):
        number = ''
        for i in j:
            number += str(i)
        if number[0] != '0' and is_eleven_multiplier(int(number)):
            result += 1
    print("THE RESULT IS: ", result)


def is_eleven_multiplier(n):
    even_sum = 0
    uneven_sum = 0
    length = len(str(n))
    for j in range(0, length):
        if j % 2 == 0:
            even_sum += int(str(n)[j])
        else:
            uneven_sum += int(str(n)[j])
    if even_sum - uneven_sum == 0 or (even_sum - uneven_sum) % 11 == 0:
        return True
    else:
        return False


generate_double_palindrome(numbers)