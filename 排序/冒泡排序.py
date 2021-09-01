def quickSortThree(start, end):
    if start >= end:
        return
    left, right = start, end
    i = start + 1
    v = nums[start]

    while i <= right:
        if nums[i] < v:
            nums[i], nums[left] = nums[left], nums[i]
            i, left = i + 1, left + 1
        elif nums[i] > v:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i = i + 1
    quickSortThree(start, left - 1)
    quickSortThree(right + 1, end)


def quickSort(start, end):
    """快速排序"""
    if start >= end:
        return
    left, right = start, end
    while left < right:
        while left < right and nums[right] >= nums[start]:
            right -= 1
        while left < right and nums[left] < nums[start]:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]
    nums[start], nums[left] = nums[left], nums[start]
    quickSort(start, left - 1)
    quickSort(left + 1, end)


def quickSort1(start, end):
    if start >= end:
        return
    left, right = start, end
    while left < right:
        while left < right and nums[right] >= nums[start]:
            right -= 1
        while left < right and nums[left] <= nums[start]:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]
    nums[left], nums[start] = nums[start], nums[left]

    quickSort1(start, left - 1)
    quickSort1(left + 1, end)


nums = [7, 5, 6, 8, 8, 1, 10]
quickSort(0, len(nums) - 1)
print(nums)
nums = [7, 5, 6, 8, 8, 1, 10]
quickSort1(0, len(nums) - 1)
print(nums)
