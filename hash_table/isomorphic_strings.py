class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param s:
        :param t:
        :return:
        """
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
        print(s_to_t)
        print(t_to_s)

        return True


if __name__ == '__main__':
    test_solution = Solution()
    s = "paper"
    t = "title"
    print(test_solution.isIsomorphic(s, t))
