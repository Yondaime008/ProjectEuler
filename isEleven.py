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
        print("isElevenMultiplier")
    else:
        print("NotElevenMultiplier")

is_eleven_multiplier(40561817703823564929)