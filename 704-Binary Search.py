704-Binary Search
# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

#  Time complexity: O(logN), N is size of input
#  Space complexity: O(1), using pointers only
#  Take-away: Be very careful about the boundary, especially with the 
#  "right" pointer.