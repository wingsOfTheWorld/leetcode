class Solution:
    def containsDuplicate(self, nums) -> bool:
        """
        Time Complexity is O(N), space complexity is O(N)
        :param nums:
        :return:
        """
        hash_map = {}
        for index, i in enumerate(nums):
            if i not in hash_map:
                hash_map[i] = index
            else:
                return True
        return False


if __name__ == '__main__':
    test_solution = Solution()
    nums = [2, 7, 11, 15]
    print(test_solution.containsDuplicate(nums))
