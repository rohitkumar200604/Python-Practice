student = {
    "name": "Rohan",
    "age": 18,
    "grade": "A"
}

profile = {
    "username": "rohankumar01",
    "details": {
        "followers": 130,
        "verified": True
    }
}

#Create a dictionary named marks to store marks of 3 subjects.
# Add the subjects one by one and print the final dictionary. 
marks = {}
for i in range(0,3):
    sub_i = input("Enter subject: ")
    mrks_i = int(input("Enter marks: "))
    marks[sub_i] = mrks_i
print("Dictionary:",marks)

# You are given a list of programming languages: 
# ["Python", "Java", "C++", "Python", "Java", "C"] 
# Convert it into a set and print how many unique languages Divya knows. 
lang = ["Python", "Java", "C++", "Python", "Java", "C"] 
set_lang = set(lang)
print("Languages in Sets:",set_lang)
print(f"Divya knows {len(set_lang)} languages")