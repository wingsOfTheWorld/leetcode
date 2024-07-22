class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Time Complexity is O(Log(N)), space complexity is O(1)
        :param nums:
        :return:
        """
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return nums[0]
            else:
                return nums[1]
        else:
            while left < right:
                middle = left + (right - left) // 2
                print(middle)
                if nums[middle] < nums[0] and nums[middle] < nums[len(nums) - 1]:
                    if middle == 0:
                        return nums[middle]
                    elif nums[middle] < nums[middle + 1] and nums[middle] < nums[middle - 1]:
                        return nums[middle]
                    else:
                        right = middle - 1
                else:
                    left = middle + 1
                    print(left)
                    if left == len(nums) - 1:
                        return min(nums[0], nums[-1])
            return nums[right]


if __name__ == '__main__':
    test_solution = Solution()
    nums = [2, 3, 1]
    test_solution.findMin(nums)
    print(test_solution.findMin(nums))
