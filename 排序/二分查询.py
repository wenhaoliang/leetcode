def binary_chop(alist, data):
    """
    非递归解决二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1

    while first <= last:
        mid = (last + first) // 2
        if alist[mid] < data:
            first = mid + 1
        elif alist[mid] > data:
            last = mid - 1
        else:
            return True

    return False


def bilibiliBinary(nums, target):
    """


    """
    n = len(nums)
    left, right = -1, n

    while left + 1 != right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid

    if 0 <= left < n:
        return True
    else:
        return False


if __name__ == "__main__":
    print(bilibiliBinary([5, 7, 7, 8, 8, 10], 11))
