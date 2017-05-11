import numpy as np
import itertools

# Iterate through all possible combinations of digit patterns
for digits in range(10, 0, -1):
    lines = [line.rstrip('\n') for line in open('TenDigitPatterns.txt')]  # Reads all digit patterns from given file
    combs = list(itertools.combinations(range(10), digits))  # Find all possible combinations of given set of digits
    for comb in combs:
        comb = list(comb)  # Convert to list
        counter = 0
        input_list = []
        for line in lines:
            if counter not in comb:
                counter += 1
                continue
            temp = [1 if i == '#' else -1 for i in line]  # Convert given pattern to bipolar transfer function values
            input_list.append(temp)
            counter += 1
        input_matrix = np.array(input_list).reshape(digits, 35)  # Convert it to NumPy frame to do matrix operations
        weight = np.dot(np.transpose(input_matrix), input_matrix)  # Find weight matrix using Hebb rule formula
        output = np.dot(input_matrix, weight)  # Find output using calculated weight
        output_list = [[0] * 35] * digits  # Generating skeleton output matrix list
        count = 0
        for row in output:
            output_list[count] = [1 if column > 0 else -1 for column in row]
            count += 1
        print(comb, 'same' if output_list == input_list else 'different')  # Print whether same or different
