class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Time Complexity is O(Log(N)), space complexity is O(1)
        :param nums:
        :param target:
        :return:
        """
        if len(nums) < 1:
            return [-1, -1]

        def find_left_index(nums, target):
            if nums[0] > target or nums[-1] < target:
                return -1
            elif nums[0] == target:
                return 0
            else:
                left = 0
                right = len(nums) - 1
                while left < right:
                    middle = left + (right - left) // 2
                    # print(middle, left, right)
                    if nums[middle] == target and nums[middle - 1] < target:
                        return middle
                    elif nums[middle] > target or (nums[middle] == target and nums[middle - 1] == target):
                        right = middle - 1
                    elif nums[middle] < target or (nums[middle] == target and nums[middle + 1] == target):
                        left = middle + 1
                if nums[right] != target:
                    return -1
                return right

        def find_right_index(nums, target):
            if nums[0] > target or nums[-1] < target:
                return -1
            elif nums[-1] == target:
                return len(nums) - 1
            else:
                left = 0
                right = len(nums) - 1
                while left < right:
                    middle = left + (right - left) // 2
                    print(middle, left, right)
                    if nums[middle] == target and nums[middle + 1] > target:
                        return middle
                    elif nums[middle] > target:
                        right = middle - 1
                    elif nums[middle] < target or (nums[middle] == target and nums[middle + 1] == target):
                        left = middle + 1
                if nums[right] != target:
                    return -1
                return right

        left_index = find_left_index(nums, target)
        # print(left_index)
        right_index = find_right_index(nums, target)
        # print(right_index)
        return [left_index, right_index]


if __name__ == '__main__':
    test_solution = Solution()
    nums = [1, 2, 3, 3, 3, 3, 4, 5, 9]
    target = 3
    print(test_solution.searchRange(nums, target))
