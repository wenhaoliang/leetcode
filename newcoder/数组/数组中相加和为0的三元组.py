"""
描述:给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。
注意：三元组（a、b、c）中的元素必须按非降序排列。（即a≤b≤c）
解集中不能包含重复的三元组。
例如，给定的数组 S = {-10 0 10 20 -10 -40},解集为(-10, -10, 20),(-10, 0, 10) 0 <= S.length <= 1000
示例1  输入：[0]                     返回值：   []
示例2  输入：[-2,0,1,1,2]            返回值：   [[-2,0,2],[-2,1,1]]
示例3  输入：[-10,0,10,20,-10,-40]   返回值：   [[-10,-10,20],[-10,0,10]]
"""


#
#
# @param num int整型一维数组
# @return int整型二维数组
#
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def threeSum(self, num):
        # write code here
        if len(num) < 3:
            return []

        num.sort()
        res = []
        for i in range(len(num) - 2):
            a = num[i]
            if i >= 1 and a == num[i - 1]:
                continue
            left, right = i + 1, len(num) - 1
            while left < right:
                if num[left] + num[right] == -a:
                    res.append([a, num[left], num[right]])
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left - 1]:
                        left += 1
                    while left < right and num[right] == num[right + 1]:
                        right -= 1
                elif num[left] + num[right] > -a:
                    right -= 1
                else:
                    left += 1
        return res


class Solution1:
    def threeSum(self, num):
        # write code here
        n = len(num)
        if n < 3:
            return None
        res = []
        num.sort()

        for i in range(n - 2):
            a = num[i]
            if i >= 1 and a == num[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                if num[left] + num[right] == -a:
                    res.append([num[i], num[left], num[right]])
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left - 1]:
                        left += 1
                    while left < right and num[right] == num[right + 1]:
                        right -= 1
                elif num[left] + num[right] > -a:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == "__main__":
    n = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    A = Solution()
    print(A.threeSum(n))
    A = Solution1()
    print(A.threeSum(n))
