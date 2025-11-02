def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "Invalid Operator"

print(calculator(8, 2, '+'))  # ✅ Output: 10
print(calculator(8, 2, '/'))  # ✅ Output: 4.0
