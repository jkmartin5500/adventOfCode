def solution():
    # Get input
    with open('./day3/input.txt') as file:
        content = file.read()

    byte_length = content.find('\n')

    # Holders for resulting values
    gamma, epsilon = ('', '')

    # Loop through directions, forward up and down increment result by corresponding distance and direction
    for i in range(byte_length):
        bits = content[i:len(content):byte_length+1]
        if bits.count('1') > len(bits) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            epsilon += '1'
            gamma += '0'

    # Return the product of horizontal and vertical distance
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    print(solution())
