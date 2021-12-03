import numpy as np


def solution():
    # Get input
    with open('./day3/input.txt') as file:
        content = file.read()

    # Bytelength for determining dominant bit and numpy arrays for oxygen and co2
    byte_length = content.find('\n')
    oxygen = np.array(content.split('\n'))
    co2 = np.copy(oxygen)

    # Loop through bytes, filter using numpy built in filter with boolean lists
    i = 0
    while i < byte_length and len(oxygen) > 1:
        bits = [j[i] for j in oxygen]
        # Keep arrays with 1 in ith place
        if bits.count('1') >= len(bits) / 2:
            oxygen = oxygen[[bit == '1' for bit in bits]]
        # Keep array with 0 in ith place
        else:
            oxygen = oxygen[[bit == '0' for bit in bits]]
        i += 1

    # Loop through bytes, filter using numpy built in filter with boolean lists
    i = 0
    while i < byte_length and len(co2) > 1:
        bits = [j[i] for j in co2]
        # Keep arrays with 1 in ith place
        if bits.count('1') < len(bits) / 2:
            co2 = co2[[bit == '1' for bit in bits]]
        # Keep array with 0 in ith place
        else:
            co2 = co2[[bit == '0' for bit in bits]]
        i += 1

    # Return the product of horizontal and vertical distance
    return int(oxygen[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    print(solution())
