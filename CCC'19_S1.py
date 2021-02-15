from copy import deepcopy

original = [[1, 2], [3, 4]]
flips = list(input())
V_num = 0
H_num = 0
for char in flips:
    if char == 'V':
        V_num += 1
    else:
        H_num += 1

modified = deepcopy(original)

if V_num % 2 != 0:
    modified[0][0] = original[0][1]
    modified[0][1] = original[0][0]
    modified[1][0] = original[1][1]
    modified[1][1] = original[1][0]

original = deepcopy(modified)
if H_num % 2 != 0:
    modified[0][0] = original[1][0]

    modified[0][1] = original[1][1]
    modified[1][0] = original[0][0]

    modified[1][1] = original[0][1]

output = ''
for i in range(len(modified)):
    for y in range(len(modified[i])):
        output += str(modified[i][y])
        if y != len(modified[i]):
            output += ' '

    output += '\n'
print(output)
