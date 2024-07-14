class Solution:
    def longestConsecutive(self, nums) -> int:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param nums:
        :return:
        """
        if not nums:
            return 0
            # 初始化哈希表
        num_map = {}
        max_length = 0
        for num in nums:
            if num not in num_map:
                left = num_map.get(num - 1, 0)
                right = num_map.get(num + 1, 0)
                # 当前序列的长度
                current_length = left + right + 1
                # 更新最大长度
                max_length = max(max_length, current_length)
                # 更新哈希表
                num_map[num] = current_length
                # 更新序列的边界值
                num_map[num - left] = current_length
                num_map[num + right] = current_length
        return max_length


if __name__ == '__main__':
    test_solution = Solution()
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(test_solution.longestConsecutive(nums))
