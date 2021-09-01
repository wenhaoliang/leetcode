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


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 11

    print(binary_chop(nums, target))
