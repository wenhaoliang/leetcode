"""
给出一个整数数组 和有序的整数数组 ，请将数组 合并到数组 中，变成一个有序的升序数组
注意：
1.可以假设 数组有足够的空间存放 数组的元素， 和 中初始的元素数目分别为 和 ，的数组空间大小为 +
2.不要返回合并的数组，返回是空的，将数组 的数据合并到里面就好了
3.数组在[0,m-1]的范围也是有序的
例1:
A: [1,2,3,0,0,0]，m=3
B: [2,5,6]，n=3
合并过后A为:
A: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, A, m, B, n):
        A[:] = sorted(A[:m] + B)
        print(A[:])


# class Solution1:
#     def merge(self, nums1, nums1Len: int, nums2, nums2Len: int):
#         res = []
#         p1, p2 = 0, 0
#         while p1 < nums1Len or p2 < nums2Len:
#             if p1 == nums1Len:
#                 res.append(nums2[p2])
#                 p2 += 1
#             elif p2 == nums2Len:
#                 res.append(nums1[p1])
#                 p1 += 1
#             elif nums1[p1] < nums2[p2]:
#                 res.append(nums1[p1])
#                 p1 += 1
#             else:
#                 res.append(nums2[p2])
#                 p2 += 1
#         nums1[:] = res
#         return res


class Solution1:
    def merge(self, A, m, B, n):
        res = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                res.append(B[p2])
                p2 += 1
            elif p2 == n:
                res.append(A[p1])
                p1 += 1
            elif A[p1] < B[p2]:
                res.append(A[p1])
                p1 += 1
            else:
                res.append(B[p2])
                p2 += 1
        A[:] = res
        return res


class Solution2:
    def merge(self, A, m, B, n):
        res = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                res.append(B[p2])
                p2 += 1
            elif p2 == n:
                res.append(A[p1])
                p1 += 1
            elif A[p1] < B[p2]:
                res.append(A[p1])
                p1 += 1
            else:
                res.append(B[p2])
                p2 += 1
        A[:] = res
        return res

if __name__ == "__main__":
    n, m = [1, 2, 3], [2, 5, 6]
    solution = Solution2()
    print(solution.merge(n, len(n), m, len(m)))
