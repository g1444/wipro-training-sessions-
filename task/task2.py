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
    
try:
    num1 = float(input())
    num2 = float(input())
    num = float(input())
except Exception as e:
    print(f"An err occurred: {e}")
    exit()

print(perform_division(num1, num2))
print(perform_square_root(num))