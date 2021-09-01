class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        rk, ans = -1, 0
        for i in range(len(s)):
            if i != 0:
                occ.remove(s[i - 1])

            while rk + 1 < len(s) and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1

            ans = max(ans, len(occ))

        return ans


if __name__ == "__main__":
    arr = 'abcc'
    A = Solution()
    print(A.lengthOfLongestSubstring(arr))
