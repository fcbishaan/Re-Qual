import unittest
from parameterized import parameterized
from Solution import Solution
from parameterized import parameterized 


class TestSlidingWindowMaximum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_example2(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_custom1(self):
        nums = [7, 6, 5, 4, 3, 2, 1]
        k = 3
        expected = [7, 6, 5, 4, 3]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_custom2(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 4
        expected = [4, 5, 6, 7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_boundary_min_length(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_boundary_max_length(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = len(nums)
        expected = [7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_equivalence_smallest_partition(self):
        nums = [1, 2, 3]
        k = 2
        expected = [2, 3]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    def test_equivalence_largest_partition(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 5
        expected = [5, 6, 7]
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

    # Additional Parameterized Tests

    # New parameterized test cases
    @parameterized.expand([
        ([1, 2, 3, 4], 2, [2, 3, 4]),
        ([7, 6, 5, 4, 3], 2, [7, 6, 5, 4]),
        ([1, 3, 5, 7], 1, [1, 3, 5, 7]),
        ([9, 7, 5, 3], 3, [9, 7]),
        ([5, 5, 5, 5, 5], 2, [5, 5, 5, 5]),
        ([1, 2, 3, 4, 5, 6], 4, [4, 5, 6]),
        ([1, 2, 3, 4, 5, 6], 6, [6]),
        ([1, 2, 3, 4, 5, 6], 7, []),
        ([], 3, []),  # Empty array
        ([1, 1, 1, 1], 4, [1]),  # All elements are the same
        ([4, 3, 2, 1], 4, [4]),  # Elements in descending order
        ([1, 2, 3, 4], 1, [1, 2, 3, 4]),  # k equal to 1
        ([1, 2, 3, 4], 4, [4]),  # k equal to array length
        ([1, 1, 2, 2, 3, 3], 3, [2, 2, 3, 3]),  # Duplicate elements
        ([1, 2, -1, 4, 5, -2, 3], 3, [2, 4, 5, 5, 5]),  # Negative values
    ])
    def test_additional_cases(self, nums, k, expected):
        self.assertEqual(self.solution.maxSlidingWindow(nums, k), expected)

if __name__ == '__main__':
    unittest.main()
