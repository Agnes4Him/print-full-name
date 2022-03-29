# PRINT FULL NAME

file = open("name.txt")
line = file.readline()
names = line.split()

# Print names in a single line
for name in names:
    print (name, end=" ")

# Print individual name
first_name = names[0]
print (first_name)
middle_name = names[1]
print (middle_name)
last_name = names[2]
print (last_name)

file.close()