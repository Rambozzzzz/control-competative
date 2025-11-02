nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = list(map(lambda x: x ** 2, nums))
multiples = list(filter(lambda x: x % 3 == 0, squares))
print("Squares:", squares)
print("Multiples of 3:", multiples)
