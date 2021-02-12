import sys

rows = int(input())
column = int(input())
number_list = [0] * rows
over = False
for numbers in range(rows):
    number_list[numbers] = list(input().split())

for one in range(rows):
    for two in range(column):
        number_list[one][two] = int(number_list[one][two])

current_number = number_list[0][0]


def check_root(c_num, num_list):
    for row in range(rows):
        for clm in range(column):
            if c_num == (row + 1) * (clm + 1) and num_list[row][clm] != 0:
                if row + 1 == rows and column == clm + 1:
                    return True

                num = number_list[row][clm]
                n_list = num_list
                n_list[row][clm] = 0
                if check_root(num, n_list):
                    return True

    return False


def main():
    global over
    over = check_root(current_number, number_list)

    if over:
        print("yes")
    else:
        print("no")


sys.setrecursionlimit(int(1e5 + 5))
main()
