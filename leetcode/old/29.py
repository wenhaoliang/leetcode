from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
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

        return res


A = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(A.spiralOrder(matrix))
