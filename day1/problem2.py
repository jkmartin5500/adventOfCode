# Get input
with open('./day1/input1.txt') as file:
    content = file.read()

# Parse input
depths = [int(depth) for depth in content.split('\n')]

# Count number of increases between indices
# Each 3 window shares the 2 last and 2 first of the window, only need to compare first and last
increases = 0
for i in range(0, len(depths)-3):
    if depths[i+3] > depths[i]:
        increases += 1

# Print result
print(increases)