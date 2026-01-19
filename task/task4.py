def ensure_int(func):
    def wrapper(self, *args):
        if not isinstance(self.num1, int) or not isinstance(self.num2, int):
            raise ValueError("Inputs must be integers")
        return func(self, *args)
    return wrapper


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @ensure_int
    def performAdd(self):
        print("Addition:", self.num1 + self.num2)

    @ensure_int
    def performSubtract(self):
        print("Subtraction:", self.num1 - self.num2)

    @ensure_int
    def performMultiply(self):
        print("Multiplication:", self.num1 * self.num2)

    def performDivide(self):
        if self.num2 == 0:
            print("Err: Division by zero is not allowed.")
        else:
            print("Division:", self.num1 // self.num2)
# Non editable starts here
if __name__ == "__main__":
    inputs = []

    while len(inputs) < 2:
        line = input().strip()
        if line:
            inputs.append(line)

    n1, n2 = map(int, inputs)

    calc = Calculator(n1, n2)
    calc.performAdd()
    calc.performSubtract()
    calc.performMultiply()
    calc.performDivide()
# Non editable ends here
