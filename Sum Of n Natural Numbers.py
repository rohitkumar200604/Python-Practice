n = int(input("Enter n for sum of first n Natural Numbers: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"Sum of first {n} Natural Numbers:",sum)