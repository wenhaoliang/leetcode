"""
给定一个整形数组arr，已知其中所有的值都是非负的，将这个数组看作一个容器，请返回容器能装多少水。
示例1 输入：[3,1,2,5,2,4] 返回值：5
示例2 输入：[4,5,1,3,2]   返回值：2
"""


#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:
    def maxWater(self, arr):
        # write code here
        if len(arr) < 2:
            return 0
        maxDepth = max(arr)
        maxIndex = arr.index(maxDepth)
        leftHand = arr[0]
        rightHand = arr[-1]
        result = 0
        for val in arr[1:maxIndex]:
            if val < leftHand:
                result += (leftHand - val)
            else:
                leftHand = val
        for val in arr[maxIndex + 1:-1][::-1]:
            if val < rightHand:
                result += (rightHand - val)
            else:
                rightHand = val
        return result


class Solution1:
    def maxWater(self, arr):
        # write code here
        if len(arr) < 2:
            return 0
        maxDepth = max(arr)
        maxIndex = arr.index(maxDepth)
        leftHand = arr[0]
        rightHand = arr[-1]
        result = 0
        for i in arr[1:maxIndex]:
            if i < leftHand:
                result += (leftHand - i)
            else:
                leftHand = i

        for i in arr[maxIndex + 1:-1][::-1]:
            if i < rightHand:
                result += (rightHand - i)
            else:
                rightHand = i

        return result


if __name__ == "__main__":
    matrix = [3, 1, 2, 5, 2, 4]
    A = Solution1()
    print(A.maxWater(matrix))
    print(A.maxWater([4,5,1,3,2] ))
