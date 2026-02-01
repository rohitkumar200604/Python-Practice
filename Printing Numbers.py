# Ascending Order
i = 1
while i<=10:
    print(i)
    i += 1

#Descending Order
i = 10
while i>=1:
    print(i)
    i -= 1

#for loop
#Descending Order
for i in range(100,0,-1):
    print(i)

def show(num):
    if num == 1:
        return print(1)
    print(num)
    return show(num-1)

n = int(input("Enter the nth number: "))
show(n)
