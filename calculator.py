def calculate(a, b, operator):
    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    return "Invalid operator"


if __name__ == "__main__":
    print("Simple Calculator")