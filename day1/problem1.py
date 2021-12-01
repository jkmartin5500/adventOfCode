# Get input
with open('./day1/input1.txt') as file:
    content = file.read()

# Parse input
depths = [int(depth) for depth in content.split('\n')]

# Count number of increases between indices
increases = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        increases += 1

# Print result
print(increases)