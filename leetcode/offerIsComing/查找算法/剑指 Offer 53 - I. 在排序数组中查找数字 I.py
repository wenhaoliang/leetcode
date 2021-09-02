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


class Solution1:
    def search(self, nums, target: int):
        def helper(tar):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= tar:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        a = helper(target)
        b = helper(target - 1)
        return a - b


class Solution2:
    def search(self, nums, target: int) -> int:
        """
        这个做法是定好红蓝边界，判断函数为isBlue(),
        即isBlue()返回为真代表左边的都是蓝色区域
        最后的返回值left为左边界最右边，
        right为右边界最左边
        """

        def isBlue(a, b):
            if a <= b:
                return True
            else:
                return False

        def helper(tar):
            n = len(nums)
            left, right = -1, n

            while left + 1 != right:
                mid = (left + right) // 2
                if nums[left] <= tar:
                    left = mid
                else:
                    right = mid

            return left

        a = helper(target)
        b = helper(target - 1)
        return a - b


class Solution3:
    def search(self, nums, target: int):
        def helper(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        a = helper(target)
        print(a)

        b = helper(target - 1)
        print(b)
        return a - b



if __name__ == "__main__":
    """
    输入: nums = [1, 2, 3, 4, 7, 7], target = 7
    输出: 6
    
    本质上看， helper() 函数旨在查找数字 tartar 在数组 nums 中的 插入点 ，
    且若数组中存在值相同的元素，则插入到这些元素的右边。  
    """
    A = Solution()
    nums = [7, 7, 7, 7, 7, 7]
    target = 7
    print(A.search(nums, target))

    A = Solution3()
    nums = [ 7]
    target = 7
    print(A.search(nums, target))
