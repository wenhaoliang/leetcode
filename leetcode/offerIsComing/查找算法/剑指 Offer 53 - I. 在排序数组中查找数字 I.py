"""
统计一个数字在排序数组中出现的次数。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
提示：
0 <= nums.length <= 105
-109<= nums[i]<= 109
nums是一个非递减数组
-109<= target<= 109
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
"""


class Solution:
    def search(self, nums, target: int):
        def helper(target):
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] <= target:
                    i = mid + 1
                else:
                    j = mid - 1
            return i
        a = helper(target)
        b = helper(target - 1)
        return a - b


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
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    """
    输入: nums = [7, 7, 7, 7, 7, 7], target = 7
    输出: 2
    
    本质上看， helper() 函数旨在查找数字 tartar 在数组 nums 中的 插入点 ，
    且若数组中存在值相同的元素，则插入到这些元素的右边。  
    """
    A = Solution()
    nums = [7, 7, 7, 7, 7, 7]
    target = 7

    print(A.search(nums, target))
