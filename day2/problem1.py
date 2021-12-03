def solution():
    # Get input
    with open('./day2/input.txt') as file:
        content = file.read()

    # Parse input
    directions = content.split('\n')

    # Tallies for distances
    horizontal, vertical = (0,0)

    # Loop through directions, forward up and down increment result by corresponding distance and direction
    for direction in directions:
        distance = int(direction.split(' ')[-1])
        if direction.startswith('f'):
            horizontal += distance
        elif direction.startswith('d'):
            vertical += distance
        else:
            vertical -= distance

    # Return the product of horizontal and vertical distance
    return horizontal * vertical


if __name__ == "__main__":
    print(solution())
