class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Time Complexity is O(NlogN), space complexity is O(N)
        :param s:
        :return:
        """
        # 统计字符频率
        hash_map = {}
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        # 将频率字典转换为列表，并按频率降序排序
        print(hash_map.items())
        sorted_chars = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)
        print(sorted_chars)

        # 构造结果字符串
        result = ''.join([char * count for char, count in sorted_chars])

        return result


if __name__ == '__main__':
    test_solution = Solution()
    s = "aaatree"
    print(test_solution.frequencySort(s))
