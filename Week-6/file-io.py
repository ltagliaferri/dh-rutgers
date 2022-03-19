# Program to work with file input / output (i/o)

# This is pulling the days.txt file in this directory in this repo
path = 'days.txt'
days_file = open(path,'r')
days = days_file.read()


new_path = 'new_days.txt'
new_days = open(new_path,'w')

title = 'Days of the Week\n'
new_days.write(title)
print(title)

new_days.write(days)
print(days)

days_file.close()
new_days.close()