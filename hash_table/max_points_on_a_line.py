class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """
        Time Complexity is O(N**2), space complexity is O(N)
        :param points:
        :return:
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def slope(p1, p2):
            dx, dy = p1[0] - p2[0], p1[1] - p2[1]
            if dx == 0:
                return (0, 1)  # 垂直线
            if dy == 0:
                return (1, 0)  # 水平线
            d = gcd(dx, dy)
            return dx // d, dy // d

        max_points = 1
        for i in range(len(points)):
            slopes = {}
            for j in range(i+1, len(points)):
                if slope(points[i], points[j]) in slopes:
                    slopes[slope(points[i], points[j])] += 1
                else:
                    slopes[slope(points[i], points[j])] = 1
            max_points = max(max_points, max(slopes.values(), default=0)+1)
        return max_points


if __name__ == '__main__':
    test_solution = Solution()
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(test_solution.maxPoints(points))
