class Solution:
    def removeElement(self, nums, val: int) -> int:
        """
        Time Complexity is O(N), space complexity is O(1)
        :param nums:
        :param val:
        :return:
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        while len(nums) > j:
            nums.pop()


if __name__ == '__main__':
    test_solution = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    nums.remove(1)
    print(nums)
    val = 2
    print(test_solution.removeElement(nums, val))
