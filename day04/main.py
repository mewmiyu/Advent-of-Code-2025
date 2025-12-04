import numpy as np


def elves_day_four_paper_rolls(input_number, amount):
    acc_rolls = 0
    new_diagram = input_number.copy()

    dim_x, dim_y = input_number.shape
    for i in range(dim_x):
        for j in range(dim_y):
            no_rolls = 0
            if input_number[i][j] != "@":
                continue
            if j != dim_y - 1:
                no_rolls += (input_number[i][j + 1] == "@")
                if i != dim_x - 1:
                    no_rolls += (input_number[i + 1][j + 1] == "@")
            if i != dim_x - 1:
                no_rolls += (input_number[i + 1][j] == "@")
                if j != 0:
                    no_rolls += (input_number[i + 1][j - 1] == "@")
            if j != 0:
                no_rolls += (input_number[i][j - 1] == "@")
                if i != 0:
                    no_rolls += (input_number[i - 1][j - 1] == "@")
            if i != 0:
                no_rolls += (input_number[i - 1][j] == "@")
                if j != dim_y - 1:
                    no_rolls += (input_number[i - 1][j + 1] == "@")
            if no_rolls < amount:
                acc_rolls += 1
                new_diagram[i][j] = "x"
    return new_diagram, acc_rolls


if __name__ == '__main__':
    input_numbers = []
    with open("input.txt") as file:
        for line in file:
            input_numbers.append(line.strip())
    input_numbers_array = np.frombuffer(np.array(input_numbers), dtype="S4").astype(str).reshape(len(input_numbers[0]),
                                                                                                 -1)
    # result, sum_rolls = elves_day_four_paper_rolls(input_numbers_array, 4)
    # print("The new diagram is: " + "\n" + str(result))
    # print("The sum is: " + str(sum_rolls))

    # Task 2
    current_diagram, current_sum = elves_day_four_paper_rolls(input_numbers_array, 4)
    while True:
        current_diagram, result_sum = elves_day_four_paper_rolls(current_diagram, 4)
        if result_sum == 0:
            break
        dim_x, dim_y = current_diagram.shape
        current_diagram[np.where(current_diagram == "x")] = "."
        current_sum += result_sum

    print("The new diagram is: " + "\n" + str(current_diagram))
    print("The sum is: " + str(current_sum))
