for x in range(2, 11):
    isprime = "yes"

    for i in range(2, x):
        if x % i == 0:
            isprime = "no"

    if isprime == "yes":
        print (x)