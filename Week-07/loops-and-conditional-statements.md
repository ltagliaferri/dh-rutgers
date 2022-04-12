# Looping and Conditional Statements in Python

<iframe width="560" height="315" src="https://www.youtube.com/embed/AW4FNWKbMyc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Note that I overindexed on the use of `int(0)` at the end! The final program should look like this:

```python
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

```