class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Time Complexity is O(N * K*logK), space complexity is O(N * K)
        :param strs:
        :return:
        """
        anagrams = {}
        for s in strs:
            # 将字符串排序
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
        # 返回哈希表中的所有值
        return list(anagrams.values())


if __name__ == '__main__':
    test_solution = Solution()
    strs = ["ddddddddddg", "dgggggggggg"]
    print(test_solution.groupAnagrams(strs))
