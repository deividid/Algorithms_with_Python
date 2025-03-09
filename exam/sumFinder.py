def sum_finder(number, nums, target):
    if number <= target:
        print(number)

    if len(nums) <= 0:
        return

    for i in range(len(nums)):

        if number + nums[i] <= target:
            result_list = [number, nums[i]]
            print(*result_list)

            j = i + 1
            while j <= len(nums) - 1:

                if sum(result_list) + nums[j] <= target:
                    result_list.append(nums[j])
                    print(*result_list)

                elif len(result_list) >= 3 and sum(result_list[:-1]) + nums[j] <= target:
                    new_list = result_list[:-1]
                    new_list.append(nums[j])
                    print(*new_list)

                j += 1

    sum_finder(nums[0], nums[1:], target)


number_set = []

for number in input().split(', '):
    number_set.append(int(number))

target_number = int(input())

sum_finder(number_set[0], number_set[1:], target_number)
