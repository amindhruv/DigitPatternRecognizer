import numpy as np


def read_matrix():
    input_list = []
    lines = [line.rstrip('\n') for line in open('TenDigitPatterns.txt')]
    counter = 0
    for line in lines:
        # Logic to skip some digits
        if counter == 0 or counter == 2 or counter == 3 or counter == 5 or counter == 8:
            counter += 1
            continue

        # Logic to limit number of digits
        # if counter > 6:
        #     break

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


inp = read_matrix()

weight = compute_weights(inp, inp)

# For making diagonal entries of weight matrix zero
# np.fill_diagonal(weight, 0)

# Uncomment following block if you want to consider bias
# bias = [0] * 35
# for i in inp:
#     bias += i
# o = np.add(bias, np.dot(inp, weight))

check_digit =  [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1]
check_spurious = np.array(check_digit).reshape(1, 35)
output_matrix = np.dot(check_spurious, weight)

print('INPUT:')
print_pattern(check_spurious)

print('OUTPUT:')
print_pattern(output_matrix)

output_list = [[0] * 35] * 5
count = 0
for row in output_matrix:
    output_list[count] = [1 if char > 0 else -1 for char in row]
    count += 1
input_list = inp.tolist()
print('input:', check_digit)
print('output:', output_list)
print('same' if output_list == check_digit else 'different')
