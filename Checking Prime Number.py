n = int(input("Enter a number to be checked: "))
check = True
for i in range(2,n):
    if n%i == 0:
        check = False
        break
if check == False:
    print(f"{n} is a composite number")
else:
    print(f"{n} is a prime number")