''' demonstrates a simple function with parameters - Justine Lee '''

def calculate(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

print("Enter a number:")
num1 = int(input())
print("Enter another number:")
num2 = int(input())

calculate(num1, num2)

print("Something else happens now")

