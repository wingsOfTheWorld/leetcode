class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param s:
        :param t:
        :return:
        """
        hash_map = {}
        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        for i in t:
            if i not in hash_map:
                return False
            else:
                hash_map[i] -= 1
        for i in hash_map.keys():
            if hash_map[i] != 0:
                return False
        return True


if __name__ == '__main__':
    test_solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(test_solution.isAnagram(s, t))
