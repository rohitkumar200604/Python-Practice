# Write code to open a file named mydata.txt in read mode. 

f = open("mydata.txt","r")

# Open a file called report.txt in write mode.

f = open("report.txt","w")

# Create a file named saumya_info.txt using "x" mode. 

f = open("saumya_info.txt","x")

# Write a program to safely check whether a file exists before opening it. 



# Read a file named story.txt and print the full content. 
with open("story.txt", "r") as f:
    data = f.read()
    print(data)

# Read only the first line of bio.txt. 
with open("bio.txt","r") as f:
    line = f.readline()
    print(line)

# Print how many lines are present in notes.txt. 
with open("notes.txt","r") as f:
    lines = f.readlines()
    n = 0
    for i in lines:
        n += 1
    print("Number Of Lines In The File:",n)

# Write your name and class into a file named intro.txt. 
with open("intro.txt","w") as f:
    f.write("Name: Rohan Kumar")
    f.write("\nClass: 12th")
    print("Done")

# Create a file goals.txt and write 3 goals for this month. 
with open("goals.txt","w") as f:
    f.write("Goals\n\n")
    f.write("1. Goal 1\n")
    f.write("2. Goal 2\n")
    f.write("3. Goal 3\n")
    print("Done")

# Append "Completed" to an existing file status.txt. 
with open("status.txt","a") as f:
    f.write("Completed")
    print("Done")

# Use with to read the entire content of info.txt. 
with open("info.txt","r") as f:
    data = f.read()
    print(data)

# Use with to write "Hello World" in hello.txt.
with open("hello.txt", "w") as f:
    f.write("Hello World")
    print("Done")

