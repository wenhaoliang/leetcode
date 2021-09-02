"""
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。
如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
示例1：
输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
示例2：
输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
"""
from typing import List


# 无重复
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


# 有重复数字[2,1,2,2,2]
class Solution1:
    def search(self, nums: List[int], target: int):
        if not nums:
            return False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[right]:
                left += 1
                continue
            # 旋转点在[left, mid]
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 旋转点在[mid+1,right]
            else:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[right]:
                left += 1
                continue
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return False


if __name__ == "__main__":
    A = Solution1()
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 13
    print(A.search(nums, target))

    A = Solution2()
    nums = [1, 0, 1, 1, 1]
    target = 0
    print(A.search(nums, target))
    """
    当搜索有重复元素的排序数组时，我们会遇到一个问题：
    如果 nums[left] nums[mid] nums[right] 时怎么办？
    比如 [2,1,2,2,2] 和 [2,2,2,1,2]，最开始时，left 指向 第 0 位置，
    right 指向第 4 位置，mid 指向中间的 2 位置；此时三者相等都为 2。
    如果我们想找 1，而这个 1 可以在 mid 的左边也可以在 mid 的右边。
    所以就不知道该在哪个区间继续搜索。
    
    一个解决本题的办法是，我们遇到 nums[left] == nums[right] 的情况时，
    直接向右移动 left，直至 nums[left] != nums[right]。
    那这样的话，上面的例子中就变成了在 [1,2,2,2]和 [2,2,2,1]上搜索，
    1 所在的区间就可以根据 mid 和 right 的大小关系而获得了。
    
    链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/fu-xue-ming-zhu-bang-zhu-ni-geng-shen-ke-zcu0/
    """
