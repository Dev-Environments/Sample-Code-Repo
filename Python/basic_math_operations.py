def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is undefined."

# Example usage:
x, y = 10, 5
print(f"Add: {add(x, y)}")
print(f"Subtract: {subtract(x, y)}")
print(f"Multiply: {multiply(x, y)}")
print(f"Divide: {divide(x, y)}")