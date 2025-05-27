# main.py
def calculate(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"

if __name__ == "__main__":
    a = 10
    b = 5
    op = 'mul'  # Change to add, sub, div to test different operations
    result = calculate(a, b, op)
    print(f"Result of {op} between {a} and {b} is: {result}")
