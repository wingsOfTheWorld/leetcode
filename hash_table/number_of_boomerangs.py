class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        """
        Time Complexity is O(N**2), space complexity is O(N)
        :param points:
        :return:
        """
        def get_distance(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        result = 0
        for i in range(len(points)):
            distance_count = {}
            for j in range(len(points)):
                if i != j:
                    distance = get_distance(points[i], points[j])
                    if distance in distance_count:
                        distance_count[distance] += 1
                    else:
                        distance_count[distance] = 1
            for count in distance_count.values():
                if count > 1:
                    result += count * (count - 1)

        return result


if __name__ == '__main__':
    test_solution = Solution()
    points = [[0, 0], [1, 0], [2, 0]]
    print(test_solution.numberOfBoomerangs(points))  # 输出 2
