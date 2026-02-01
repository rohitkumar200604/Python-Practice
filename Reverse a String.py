str = input("Enter a word to be reversed: ")
reverse_string = ""
n = len(str)
for i in range(n-1,-1,-1):
    reverse_string += str[i]
print("Reverse String:",reverse_string)
