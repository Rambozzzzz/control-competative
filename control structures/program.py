print("Enter three numbers:")
num1 = int(input())
num2 = int(input())
num3 = int(input())

minimum = min(num1, num2, num3)
print("Minimum number is:", minimum)

print("\nEnter three angles of a triangle:")
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("Triangle is valid.")
else:
    print("Triangle is NOT valid.")

print("\nEnter five numbers:")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

average = (a + b + c + d + e) / 5
print("Average of the five numbers is:", average)

percentage = float(input("\nEnter percentage: "))

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

