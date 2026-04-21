# Loop Examples in Python

# 1. Print numbers from 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("\n")

# 2. Print even numbers from 1 to 20
print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("\n")

# 3. Sum of first N numbers
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1):
    sum += i

print("Sum is:", sum)
