#WAP to accept a number from 1 to 7 and display the name of the day, like 1 for 
#Sunday, 2 for Monday, etc.

day_number = int(input("Enter a number (1-7): "))
if day_number == 1:
    print("Sunday")
elif day_number == 2:
    print("Monday")
elif day_number == 3:
    print("Tuesday")
elif day_number == 4:
    print("Wednesday")
elif day_number == 5:  
    print("Thursday")
elif day_number == 6:
    print("Friday")
elif day_number == 7:
    print("Saturday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
    