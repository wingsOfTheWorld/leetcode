class Solution:
    def twoSum(self, nums, target: int):
        """

        :param nums:
        :param target:
        :return:
        """
        hash_map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hash_map:
                return [hash_map[another_num], index]
            hash_map[num] = index
        return []


if __name__ == '__main__':
    test_solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(test_solution.twoSum(nums, target))
