class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Time Complexity is O(N), space complexity is O(1)
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            else:
                nums[len(nums)-1-j] = 0
            i += 1
        for i in range(j, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    pass
