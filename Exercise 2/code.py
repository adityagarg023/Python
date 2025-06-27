# Import the time module to access current time
import time

# Get current time in HH:MM:SS format
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

# Extract hour from timestamp as an integer for comparison
hourstamp = int(time.strftime("%H"))

# Determine greeting based on the hour of the day
if hourstamp < 12:
    print("Good Morning")
elif hourstamp < 17:
    print("Good Afternoon")
elif hourstamp < 20:
    print("Good Evening")
else:
    print("Good Night")
