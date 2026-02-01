# Write a program that takes your favorite food name as input and prints: 
# ● The middle 3 characters 
 
# ● The last 2 characters

food_name = input("Enter your favourite food name: ")
n = len(food_name)
if type(n/2) == "integer":
    print("The middle three characters are:",food_name[(n/2-1)-1],food_name[n/2-1],food_name[(n/2-1)+1])
else:
    n2 = n//2
    print("The middle three characters are:",food_name[n2-1],food_name[n2],food_name[n2+1])
print("The last 2 characters are:",food_name[-2],food_name[-1])


# Write a program that: 
# ● Takes a sentence as input 
# ● Converts it to lowercase  
# ● Replaces all spaces " " with underscores "_" 
# ● Prints the new string

sen = input("Enter a sentence: ")
new_sen = sen.lower().replace(" ","_")
print("New Sentence is:",new_sen)

# Write a program that takes a sentence and prints: 
# ● Total characters (len()) 
# ● Uppercase version 
# ● Lowercase version 

sen = input("Enter a sentence: ")
n = len(sen)
upper_sen = sen.upper()
lower_sen = sen.lower()
print("Total Characters:",n)
print("Uppercase Version:",upper_sen)
print("Lowercase Version:",lower_sen)

# Write a Python program that takes any word or sentence as input and prints: 
# ● The first character 
# ● The last character 
# ● The total number of characters

sen = input("Enter a word or sentence: ")
print("First Character:",sen[0])
print("Last Character:",sen[-1])
print("Total Number Of Characters:",len(sen))