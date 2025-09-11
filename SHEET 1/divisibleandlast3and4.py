number = int(input("Enter a number: "))

if number % 3 == 0 and number % 10 == 4:
    print("The number is divisible by 3 and its last digit is 4.")
else:
    print("The number does not satisfy both conditions.")
