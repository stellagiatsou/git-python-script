from datetime import date

today = date.today()
print("Current date: ", today)

count = 0  # Initialize the variable

for i in range(319):
    count += 1  # Increase count
    print(f"Current count: {count}")
