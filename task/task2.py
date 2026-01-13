import math

def perform_division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Err: Division by zero is not allowed."
    except Exception as e:
        return f"An err occurred: {e}"


def perform_square_root(num):
    try:
        return math.sqrt(num)
    except ValueError:
        return "Square root of a negative number is undefined."
    except Exception as e:
        return f"An err occurred: {e}"