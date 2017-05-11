import numpy as np


def read_matrix():
    input_list = []
    lines = [line.rstrip('\n') for line in open('TenDigitPatterns.txt')]
    counter = 0
    for line in lines:
        # Logic to skip some digits
        # if counter == 3 or counter == 5:
        #     counter += 1
        #     continue

        # Logic to limit number of digits
        if counter > 4:
            break

        temp = [1 if char == '#' else -1 for char in line]
        input_list.append(temp)
        counter += 1
    input_matrix = np.array(input_list).reshape(5, 35)
    return input_matrix


def print_pattern(matrix):
    for row in matrix:
        count = 0
        for column in row:
            if count % 5 == 0:
                print()
            print('#' if column > 0 else '.', end='')
            count += 1
        print()
    print()


def print_pattern_with_zero(matrix):
    for row in matrix:
        count = 0
        for column in row:
            if count % 5 == 0:
                print()
            if column > 0:
                print('#', end='')
            elif column < 0:
                print('.', end='')
            else:
                print('0', end='')
            count += 1
        print()
    print()


def compute_weights(inp, outp):
    return np.dot(np.transpose(inp), outp)


def random_mistakes(matrix, length):
    shape = matrix.shape
    flat_array = matrix.flatten()  # Flatten to 1D
    indices = np.random.choice(flat_array.size, size=length)  # Get random indices
    flat_array[indices] = flat_array[indices] * -1  # Flip the bits
    return flat_array.reshape(shape)  # Restore original shape


def random_missing(matrix, length):
    shape = matrix.shape
    flat_array = matrix.flatten()  # Flatten to 1D
    indices = np.random.choice(flat_array.size, size=length)  # Get random indices
    flat_array[indices] = 0  # Fill with 0
    return flat_array.reshape(shape)  # Restore original shape


inp = read_matrix()

weight = compute_weights(inp, inp)

# For making diagonal entries of weight matrix zero
# np.fill_diagonal(weight, 0)

# Uncomment following block if you want to consider bias
# bias = [0] * 35
# for i in inp:
#     bias += i
# o = np.add(bias, np.dot(inp, weight))

noisy_input = random_mistakes(inp, int(len(inp)*len(inp[0])*0.15))   #Providing percentage of bits with mistakes
noisy_input = random_missing(inp, int(len(inp) * len(inp[0]) * 0.4))  # Providing percentage of bits with missing values
output_matrix = np.dot(noisy_input, weight)

# o = np.dot(inp, weight)

print('INPUT:')
print_pattern(inp)

print('NOISY INPUT:')
print_pattern_with_zero(noisy_input)

print('OUTPUT:')
print_pattern(output_matrix)

output_list = [[0] * 35] * 5
count = 0
for row in output_matrix:
    output_list[count] = [1 if char > 0 else -1 for char in row]
    count += 1
input_list = inp.tolist()
print('input:', input_list)
print('output:', output_list)
print('same' if output_list == input_list else 'different')
