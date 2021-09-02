"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
示例 1：
输入：[3,4,5,1,2]
输出：1
示例 2：
输入：[2,2,2,0,1]
输出：0
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
"""


class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                # 这里是因为numbers[m]不可能是旋转点
                i = m + 1
            elif numbers[m] < numbers[j]:
                # 这里是因为numbers[m]也可能是旋转点
                j = m
            else:
                # return min(numbers[i:j])
                j -= 1
        return numbers[i]


class Solution1:
    def minArray(self, numbers: [int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:

            mid = (left + right) // 2
            if numbers[left] == numbers[right]:
                left += 1
                continue

            if numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right = mid

        return numbers[left]


if __name__ == "__main__":
    """
    输入：[3,4,5,1,2]
    输出：1
    排序数组的查找问题首先考虑使用 二分法 解决，其可将 遍历法 的 线性级别 时间复杂度降低至 对数级别 。
    初始化： 声明 i, j 双指针分别指向 nums 数组左右两端；
    循环二分： 设 m = (i + j) / 2为每次二分的中点（ "/" 代表向下取整除法，因此恒有 i≤m<j ），可分为以下三种情况：
    当 nums[m] > nums[j]时： m 一定在 左排序数组 中，即旋转点 x 一定在 [m + 1, j] 闭区间内，因此执行 i = m + 1；
    当 nums[m] < nums[j]时： m 一定在 右排序数组 中，即旋转点 x 一定在[i, m] 闭区间内，因此执行 j = m；
    当 nums[m] = nums[j]时： 无法判断 m 在哪个排序数组中，即无法判断旋转点 x 在 [i, m]还是 [m + 1, j]区间中。
    解决方案： 执行 j = j - 1 缩小判断范围，分析见下文。
    返回值： 当 i = j时跳出二分循环，并返回旋转点的值 nums[i] 即可。
    
    实际上，当出现 nums[m] = nums[j] 时，一定有区间 [i, m]内所有元素相等 或 区间 [m, j]内所有元素相等（或两者皆满足）。
    对于寻找此类数组的最小值问题，可直接放弃二分查找，而使用线性查找替代。
    min(numbers[i:j])
    """
    A = Solution()
    nums = [3, 4, 5, 1, 2, 3]
    print(A.minArray(nums))
    A = Solution1()
    nums = [3, 4, 5, 1, 2, 3]
    print(A.minArray(nums))
