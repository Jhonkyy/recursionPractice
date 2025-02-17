def digitCounter(n):
    if n <= 9:
        return 1
    else:
        return 1 + digitCounter(n//10)

print(digitCounter(12345))