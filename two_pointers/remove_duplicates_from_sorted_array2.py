class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        Time Complexity is O(N), space complexity is O(1)
        :param nums:
        :return:
        """
        if len(nums) > 2:
            i = 2
            j = 1

            while i < len(nums):
                if nums[i] != nums[j] or nums[i] != nums[j-1]:
                    j += 1
                    nums[j] = nums[i]
                i += 1
            while len(nums) > (j + 1):
                nums.pop()
        print(nums)


if __name__ == '__main__':
    test_solution = Solution()
    # print(test_solution.select_s("abca"))
    s = [0, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    test_solution.removeDuplicates(s)
