__author__ = 'abnasser'


def ispalindrome(num):
    return str(num) == str(num)[::-1]


def find_palindrome(n):
    return int(str(n)[::-1])

n = 349
somme = 0
for n in range(1, 10**4+1):
    iteration = 0
    while iteration < 50:
        m = find_palindrome(n)
        res = n+m
        if ispalindrome(n + m):
            break
        n += m
        iteration += 1
    if iteration == 50:
        somme += 1
print(somme)

