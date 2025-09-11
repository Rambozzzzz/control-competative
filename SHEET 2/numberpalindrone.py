A = int(input("Enter a number: "))
reverse = 0
temp = A
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if A == reverse:
    print("Yes")
else:
    print("No")
