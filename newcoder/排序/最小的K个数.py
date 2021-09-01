"""
描述
给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
示例1 输入：[4,5,1,6,2,7,3,8],4 返回值：[1,2,3,4]
说明：返回最小的4个数即可，返回[1,3,2,4]也可以
示例2输入：[1],0返回值：[]
示例3输入：[0,1,2,1,2],3返回值：[0,1,1]
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k >= len(tinput) or not tinput:
            return tinput

        def quickSort(left, right):
            i, j = left, right
            while i < j:
                while i < j and tinput[j] >= tinput[left]:
                    j -= 1
                while i < j and tinput[i] <= tinput[left]:
                    i += 1
                tinput[i], tinput[j] = tinput[j], tinput[i]

            tinput[i], tinput[left] = tinput[left], tinput[i]
            if i < k:
                return quickSort(i + 1, right)
            elif i > k:
                return quickSort(left, i - 1)
            else:
                return tinput[:k]

        return quickSort(0, len(tinput) - 1)


if __name__ == "__main__":
    arr, k = [], 0
    A = Solution()
    print(A.GetLeastNumbers_Solution(arr, k))
