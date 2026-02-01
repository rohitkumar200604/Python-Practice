# Write a program that takes names of 3 favorite foods from the user and stores 
# them in a list. Then print the list and its length. 

lst = list(input("Enter food names:").split())
print("The list of foods is:",lst)
print("Length of List:",len(lst))

#ERROR

# Ask the user for their 3 favorite movies and store them in a list.

movies = list(input("Enter 3 favorite movies: ").split())
print(movies)

# Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and 
# lowest marks using max() and min(). 
marks = (87, 64, 33, 95, 76)
print("Highest Marks:",max(marks))
print("Lowest Marks:",min(marks))
