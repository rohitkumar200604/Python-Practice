n = int(input("Enter n for sum of first n Natural Numbers: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"Sum of first {n} Natural Numbers:",sum)

#Using Recursive Functions
sum_num = 0
def Sum(num):
    global sum_num
    sum_num += num
    if num == 0:
        return sum_num
    return Sum(num-1)
n = int(input("Enter n for sum of first n Natural Numbers: "))
sum_new = Sum(n)
print("Sum:",sum_new)