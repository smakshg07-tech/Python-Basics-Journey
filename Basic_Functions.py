# Function Examples

# 1. Simple function
def greet():
    print("Hello, welcome to Python!")

greet()

# 2. Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# 3. Recurrsive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
