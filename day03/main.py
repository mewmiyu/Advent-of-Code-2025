def elves_day_three_input_joltage_twelve(input_number, jump):
    largest_joltage = []
    sum_joltage = 0
    for x in input_number:
        largest_number = int(x[len(x)-jump:])
        current_id = 0
        for i in range(jump):
            start_id = current_id
            end_id = len(x) - jump + i
            change_id = end_id
            for j in range(start_id, end_id):
                if i == 0:
                    current_number = x[j] + str(largest_number)[i+1:]
                elif i == jump-1:
                    current_number = str(largest_number)[:jump-1] + x[j]
                else:
                    current_number = str(largest_number)[0:i] + x[j] + str(largest_number)[i+1:]
                final_number = int(current_number)
                if final_number > largest_number or (j <= change_id and final_number == largest_number):
                    largest_number = final_number
                    current_id = j + 1
                    change_id = j
            if start_id == current_id:
                current_id = end_id + 1
        largest_joltage.append(largest_number)
        sum_joltage += largest_number
    return largest_joltage, sum_joltage

def elves_day_three_input_joltage(input_number):
    largest_joltage = []
    sum_joltage = 0
    for x in input_number:
        highest = 0
        second_highest = 0
        for i in range(len(x)):
            current = int(x[i])
            if current > highest and i != len(x)-1:
                highest = current
                second_highest = 0
            elif current > second_highest:
                second_highest = current
        final_number = str(highest) + str(second_highest)
        largest_joltage.append(int(final_number))
        sum_joltage += int(final_number)
    return largest_joltage, sum_joltage


if __name__ == '__main__':
    input_numbers = []
    with open("input.txt") as file:
        for line in file:
            input_numbers.append(line.strip())

    #result, sum_jo = elves_day_three_input_joltage(input_numbers)
    result, sum_jo = elves_day_three_input_joltage_twelve(input_numbers, 12)
    print("The joltages are: " + str(result))
    print("The sum is: " + str(sum_jo))
