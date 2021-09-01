"""
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子piles[i]。
游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回true，当李赢得比赛时返回false。
示例：
输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
提示：
2 <= piles.length <= 500
piles.length 是偶数。
1 <= piles[i] <= 500
sum(piles)是奇数。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stone-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i] 表示A 取到第i次的时候的最大值
        n = len(piles)
        tempPlies = piles[:]
        # dp = [0] * n
        tempA, tempB, flag = 0, 0, 0
        i = 0
        for flag in range(n):
            tempMax = max(tempPlies[i], tempPlies[-1])
            if tempMax == tempPlies[i]:
                tempPlies[i] = 0
            else:
                i -= 1
                tempPlies.pop()
            if flag % 2 == 0:
                tempA = tempA + tempMax
            else:
                tempB = tempB + tempMax
            i += 1
        if tempA > tempB:
            return True
        else:
            return False


# 动态规划
# + 1. 创建一个二维数组 dp[len][len]
# + 2. dp[i][j]: i~j 组成的字数组 亚历克斯能够赢得的分数
# + 3. dp[i][j]: 这是有2个选择: 求出最大值
# 1: 亚历克斯拿走左边的i, 剩下dp[i+1][j] 就是李能够获取的最大分数, = piles[i] - dp[i+1][j]
# 2: 亚历克斯拿走右边的j, 剩下dp[i][j-1] 就是李能够获取的最大分数, = piles[j] - dp[i][j-1]
# + 4. 特例dp[i][i] 意味着只有一堆，那么肯定赢，= piles[i]

# f[i][j]表示石子在[i...j]这个区间范围内，
# 当前玩家与另外一个玩家的石子数量的差值，
# （# 当前玩家并不一定是先手玩家Alex）,
# 如果差值大于0，表示当前玩家处在当前这个节点上，
# 比另外一个玩家拿的石子多
#
# 如果拿了[i],当前玩家获取到的石子数量是piles[i],
# 而f[i+1][j]表示在[i+1....j]这个范围内，
# 另外一个玩家比当前玩家多的石子数量，
# 即f[i+1][j]（注意此时发生了反转），
# 而相反数-f[i+1][j]表示是的当前玩家比另外一个玩家多的数量，
# 也就是说f[i][j]=piles[i]+(-f[i+1][j]),
# 如果拿了[j],类似可得到f[i][j]=piles[j]+(-f[i][j-1])


class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for m, pile in enumerate(piles):
            dp[m][m] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] > 0


class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0] * n
        # tempPlies = piles[:]
        for m in range(n):
            dp[m] = piles[m]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        print(dp)
        return dp[n - 1] > 0


if __name__ == "__main__":
    amount = [3, 7, 2, 3]
    A = Solution1()
    print(A.stoneGame(amount))
