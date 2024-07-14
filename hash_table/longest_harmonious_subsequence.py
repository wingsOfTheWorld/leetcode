class Solution:
    def findLHS(self, nums) -> int:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param nums:
        :return:
        """
        hash_map = {}
        for index, num in enumerate(nums):
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        max_length = 0
        for num in hash_map:
            if (num + 1) in hash_map:
                if hash_map[num] + hash_map[num + 1] > max_length:
                    max_length = hash_map[num] + hash_map[num + 1]
        return max_length


if __name__ == '__main__':
    test_solution = Solution()
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    test_solution.findLHS(nums)
