# Write a program to read a text from a given file certificate.txt and find 
# whether it contains the word live. 

f = open("certificate.txt","r")
data = f.read().split()
for word in data:
    if word == "live":
        print("The file contains \"live\" word")
        break
else:
    print("The file does not contain \"live\" word")