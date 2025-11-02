def fun(a):
    return a % 2 == 0

sequence = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = list(filter(fun, sequence))
print(filtered)  
