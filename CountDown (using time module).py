# Print a coutdown before something "Excitng" happens
#  (like "Launching...", "Happy New Year" )

import time

count = int(input("Enter the Countdown Timer Limit: "))
print("\n CountDown Start Now... \n")
for i in range(count,0,-1):
    print(i)
    time.sleep(1)
print("\nHappy New Year\n")