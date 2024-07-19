class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        """
        Time Complexity is O(N**2), space complexity is O(N**2)
        :param nums1:
        :param nums2:
        :param nums3:
        :param nums4:
        :return:
        """
        count1 = {}
        count2 = {}

        # Count frequencies of sums in nums1 and nums2
        for num1 in nums1:
            for num2 in nums2:
                sum1 = num1 + num2
                if sum1 in count1:
                    count1[sum1] += 1
                else:
                    count1[sum1] = 1

        # Count frequencies of sums in nums3 and nums4
        for num3 in nums3:
            for num4 in nums4:
                sum2 = num3 + num4
                if sum2 in count2:
                    count2[sum2] += 1
                else:
                    count2[sum2] = 1

        result = 0

        # Check for pairs of sums that add up to zero
        for sum1 in count1:
            if -sum1 in count2:
                result += count1[sum1] * count2[-sum1]

        return result


if __name__ == '__main__':
    test_solution = Solution()
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(test_solution.fourSumCount(nums1, nums2, nums3, nums4))
