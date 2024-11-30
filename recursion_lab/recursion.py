def sum_of_array(numbs):
    if len(numbs) <= 1:
        return int(numbs.pop())

    return int(numbs.pop()) + sum_of_array(numbs)


input_numbers = input().split()

print(sum_of_array(input_numbers))