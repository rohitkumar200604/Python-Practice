i = 1
while i<=5:
    print("Hello World")
    i += 1

# Write a program to print numbers from 1 to 50, but print "Saumya Singh" 
# instead of numbers that are multiples of 5. 
for i in range(1,51):
    if i%5 == 0:
        print("Saumya Singh")
    else:
        print(i)

# Write a program that prints numbers 1 to 10, but skips the number 7 using the 
# continue statement.

for i in range(1,11):
    if i == 7:
        continue
    else:
        print(i)