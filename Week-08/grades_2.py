# Modifying grades.py from last week, dictionary to two lists with zip()

students = ["Dante", "Leopardi", "Ariosto", "Galileo", "Tasso"]
grades = [100, 55, 66, 75, 88]


for s, g in zip(students, grades):
    # Check if grade is passing first
    if g >= 65:
        if g >= 90:
            print(s + " got an A.")
        elif g >= 80:
            print(s + " got a B.")
        elif g >= 65:
            print(s + " got a C.")
    else:
        print(s + " failed.")
