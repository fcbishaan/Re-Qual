import unittest
from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

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

if __name__ == '__main__':
    unittest.main()
