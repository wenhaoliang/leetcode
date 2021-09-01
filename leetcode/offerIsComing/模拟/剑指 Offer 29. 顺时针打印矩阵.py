"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
"""


class Solution:
    def spiralOrder(self, matrix):
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        res = []

        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                return res

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                return res

            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                return res

            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                return res


if __name__ == "__main__":
    """
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]
    """
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    a = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    b = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    A = Solution()
    print(A.spiralOrder(matrix))
