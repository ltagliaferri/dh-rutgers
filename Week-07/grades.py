grades = {"Dante": 100, "Leopardi": 55, "Ariosto": 66, "Galileo": 75, "Tasso": 88}

for key, value in grades.items():
    # Check if grade is passing first
    if value >= 65:
        if value >= 90:
            print(key + " got an A.")
        elif value >= 80:
            print(key + " got a B.")
        elif value >= 65:
            print(key + " got a C.")
    else:
        print(key + " failed.")
