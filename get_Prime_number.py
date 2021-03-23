count = 0
limit = 100
i = 2
while count < limit and i >= 2:
    isPrime = True
    j = 2
    while i > j:
        if i % j == 0:
            isPrime = False
        j += 1
    if isPrime:
        print(i, end=" ")
    i += 1
    count += 1