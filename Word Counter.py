file = input("Enter filename with extension to count words: ")
with open(file, "r") as f:
    data = f.read().split()
    n = 0
    for words in data:
        n += 1
    print("Word Count:",n)