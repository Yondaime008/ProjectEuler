import time


n = 40561817703823564929


tic = time.clock()

string = str(n)
while len(string) > 2:
    string_result = ""
    for i in range(0, len(string)):
        if i < len(string)-1:
            string_result += string[i]
    string_result = str(int(string_result)-int(string[i]))
    string = string_result

if int(string_result) % 11 == 0 or int(string_result == 0):
    print("11 MULTIPLIER")

toc = time.clock()
print("TIME CONSUMED",(toc - tic)," s")
