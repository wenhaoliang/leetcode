def merge(nums, left, mid, right):
    i, j, temp = left, mid + 1, []
    while i <= mid and j <= right:
        if nums[i] >= nums[j]:
            #
            temp.append(nums[j])
            j += 1
        else:
            temp.append(nums[i])
            i += 1

    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= right:
        temp.append(nums[j])
        j += 1

    for i in range(len(temp)):
        nums[left+i] = temp[i]


def mergeSort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    mergeSort(nums, left, mid)
    mergeSort(nums, mid + 1, right)
    merge(nums, left, mid, right)

if __name__ == "__main__":
    a = [7, 5, 6, 4]
    mergeSort(a, 0, len(a) - 1)
    print(a)
