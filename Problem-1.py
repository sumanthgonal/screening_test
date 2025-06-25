class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            return self.a / self.b if self.b != 0 else "Division by zero error"
        else:
            return "Invalid operation"

# Example
calc = Calculator(10, 2, "divide")
print(calc.calculate())
