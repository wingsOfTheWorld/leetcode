class Solution:
    def select_s(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return [i, j]
        return False

    def validPalindrome(self, s: str) -> bool:
        """
        Time Complexity is O(N), space complexity is O(1)
        :param s:
        :return:
        """
        result = self.select_s(s)
        # print(result)
        if result:
            i = result[0]
            j = result[1]
            s1 = s[0:j:] + s[j+1::]
            s2 = s[0:i:] + s[i+1::]
            if self.select_s(s1) and self.select_s(s2):
                return False
            else:
                return True
        else:
            return True


if __name__ == '__main__':
    test_solution = Solution()
    # print(test_solution.select_s("abca"))
    print(test_solution.validPalindrome("ebcbbececabbacecbbcbe"))
