from datetime import datetime

now = datetime.today()
with open("datetime.txt", "w") as file:
    file.write(f"Local date and time: {now}\n")