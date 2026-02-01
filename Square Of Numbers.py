n = int(input("Enter the number till which squares are required: "))
for i in range(1,n+1):
    print(i**2)

#Using Function
def square(num):
    sq_num = num**2
    return sq_num

n = int(input("Enter the number for its square: "))
sq_num = square(n)
print(f"The square of {n}:",sq_num)