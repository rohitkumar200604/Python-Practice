def fibonacci(n): 
    if n <= 1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2) 
 
n = int(input("Enter the end of Fibonacci Series: "))
for i in range(n+1): 
    print(fibonacci(i), end=" ")