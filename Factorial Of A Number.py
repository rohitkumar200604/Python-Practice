# Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

n = int(input("Enter a number to get its factorial: "))
fact = factorial(n)
print("Factorial:",fact)

# Using For Loop
n = int(input("Enter a number to get its factorial: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial is:",fact)