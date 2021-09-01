from heapq import *

if __name__ == "__main__":
    # Python 中 heapq 模块是小顶堆。实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反 即可。
    A = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
    B = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
    heapify(A)
    heapify(B)
    print('初始', B)
    B = [-B[i] for i in range(len(B))]
    print('- ', B)
    print('初始', A)

    heappop(A)
    print('pop', A)
    print('-pop', B)
