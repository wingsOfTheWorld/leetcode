class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Time Complexity is O(N), space complexity is O(1)
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1
        i = 0
        j = 0
        max_length = 0
        while j <= (len(nums) - 1):
            if nums[j] == 0:
                i = j
            else:
                if nums[i] == 0:
                    max_length = max(max_length, j - i)
                else:
                    max_length = max(max_length, j - i + 1)
            j += 1
        return max_length


if __name__ == '__main__':
    test_solution = Solution()
    nums = [0, 1, 1, 0, 1]
    print(test_solution.findMaxConsecutiveOnes(nums))
