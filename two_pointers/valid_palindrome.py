class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param s:
        :return:
        """
        s_new = ''.join([i.lower() for i in s if i.isalnum()])
        print(s_new)
        if ''.join(reversed(s_new)) == s_new:
            return True
        else:
            return False


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.isPalindrome("0P"))
