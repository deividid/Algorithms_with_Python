def quick_sort(nums, start, end):
    if start >= end:
        return

    pivot, left, right = start, start + 1, end
    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    quick_sort(nums, start, right - 1)
    quick_sort(nums, right + 1, end)

    return nums


data = [int(num) for num in input().split(" ")]
print(*quick_sort(data, 0, len(data) - 1), sep=" ")
