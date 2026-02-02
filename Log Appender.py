# Append the current date and time to a file logs.txt whenever the program runs. 
import datetime
with open("logs.txt","a") as f:
    f.write(f"Logged In at {datetime.datetime.now()}\n")
    print("Log Added...")
