x = int(input("Enter first angle: "))
y = int(input("Enter second angle: "))
z = int(input("Enter third angle: "))

if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print("Triangle is valid")
else:
    print("Triangle is not valid")
