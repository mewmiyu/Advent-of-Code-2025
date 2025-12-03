def elves_day_two_invalid_id_multiple(input_number):
    same_numbers = []
    sum_numbers = 0
    seen_numbers = set(same_numbers)
    for x in input_number:
        a = int(x.split("-")[0])
        b = int(x.split("-")[1])
        div = int(len(str(b)) / 2)
        while a <= b:
            for i in range(1, div+1):
                for j in range(0, int(len(str(a))), i):
                    if not str(a)[j+i:j+i+i] and j != 0:
                        if a not in seen_numbers:
                            seen_numbers.add(a)
                            same_numbers.append(a)
                            sum_numbers += a
                    if str(a)[j:j+i] != str(a)[j+i:j+i+i]:
                        break
            a += 1
    return same_numbers, sum_numbers


def elves_day_two_invalid_id(input_number):
    same_numbers = []
    sum_numbers = 0
    for x in input_number:
        a = int(x.split("-")[0])
        b = int(x.split("-")[1])
        div = int(len(str(b)) / 2)
        while a <= b:
            if str(a)[0:div] == str(a)[div:]:
                same_numbers.append(a)
                sum_numbers += a
            a += 1
    return same_numbers, sum_numbers

if __name__ == '__main__':
    with open("input.txt") as file:
        input_numbers = file.read().split(',')

    #result, sum_no = elves_day_two_invalid_id(input_numbers)
    result, sum_no = elves_day_two_invalid_id_multiple(input_numbers)
    print("The invalid IDs are: " + str(result))
    print("The sum is: " + str(sum_no))
