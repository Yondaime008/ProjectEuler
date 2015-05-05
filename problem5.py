def isDividable(x):
    for i in range(1,20):
        if(x%i!=0):
            test=False
    if (test):
        return True
    else:
        return False

x=20
test = True
while(test):
    x=x+1
    if(isDividable(x)):
        print("FOUND IT")
        print(x)
        test = False
