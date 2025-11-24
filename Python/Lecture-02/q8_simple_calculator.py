# Simple Calculator

def calculator(a, b, operation):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return "Invalid operator"
        
print(calculator(2, 2, "+"))
