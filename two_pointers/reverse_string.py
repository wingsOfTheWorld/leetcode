class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        Time Complexity is O(N), space complexity is O(1)
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)


if __name__ == '__main__':
    test_solution = Solution()
    # print(test_solution.select_s("abca"))
    s = ["h","e","l","l","o"]
    test_solution.reverseString(s)
