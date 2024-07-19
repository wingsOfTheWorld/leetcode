class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Time Complexity is O(N**2), space complexity is O(N)
        :param nums:
        :return:
        """
        nums.sort()
        result_list = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复元素

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result_list.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # 跳过重复元素
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # 跳过重复元素
                    left += 1
                    right -= 1

        return result_list


if __name__ == '__main__':
    test_solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]

    print(test_solution.threeSum(nums))
