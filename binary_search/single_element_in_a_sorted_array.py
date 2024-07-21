class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        Time Complexity is O(Log(N)), space complexity is O(1)
        :param nums:
        :return:
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            # print(middle)
            if nums[middle - 1] != nums[middle] and nums[middle + 1] != nums[middle]:
                return nums[middle]
            if nums[middle - 1] == nums[middle]:
                if not len(nums[:middle]) % 2:
                    right = middle
                else:
                    left = middle + 1
            else:
                if len(nums[:middle]) % 2:
                    right = middle
                else:
                    left = middle + 1
        return nums[right]


if __name__ == '__main__':
    test_solution = Solution()
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(test_solution.singleNonDuplicate(nums))
