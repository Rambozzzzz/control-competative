n = int(input("Enter number of students: "))
marks = list(map(int, input("Enter marks: ").split()))[:n]

p = 0   
f = 0   

for m in marks:
    if m >= 35:
        p += 1
    else:
        f += 1

print("Pass:", p, "Fail:", f)
