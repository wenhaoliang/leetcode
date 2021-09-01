class Solution:
    def Fibonacci(self, n):
        # write code here
        f = [0] * (n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]


if __name__ == "__main__":
    n = 0
    A = Solution()
    print(A.Fibonacci(n))
