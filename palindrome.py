def isPalindrome(n):
    result = True
    i=0
    j=0
    for y,c in zip(str(n), reversed(str(n))):
        if(y!=c):
            result= False
    return result
max = 1
for x in range(0,999):
    for y in range (0,x):
        var = x*y
        if(isPalindrome(var) and var>max):
            max = var
print(max)
