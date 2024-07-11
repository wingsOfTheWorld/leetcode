class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Time Complexity is O(N), space complexity is O(1)
        :param s:
        :return:
        """
        reverse_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_len = len(s)
        i = 0
        j = s_len - 1
        while i < j:
            if s[i] not in reverse_list:
                i += 1
            else:
                if s[j] not in reverse_list:
                    j -= 1
                else:
                    s = s[0:i:] + s[j] + s[i+1:j:] + s[i] + s[j+1::]
                    i += 1
                    j -= 1
        return s


if __name__ == '__main__':
    test_solution = Solution()
    print(test_solution.reverseVowels('leetcode'))