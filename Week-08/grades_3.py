# Modifying grades.py to be a function

def calculate_grades(): 
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

students = ["Dante", "Leopardi", "Ariosto", "Galileo", "Tasso"]
grades = [100, 55, 66, 75, 88]

calculate_grades()

