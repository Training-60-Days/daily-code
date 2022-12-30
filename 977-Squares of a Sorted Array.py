977-Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # populate a dummy res list, update values from the end of the list
        res = [0] * len(nums) 
        ind = len(res) - 1
        L = 0
        R = len(nums) - 1

        while L <= R:
            nL = nums[L] ** 2
            nR = nums[R] ** 2

            if nL > nR:
                res[ind] = nL
                L += 1
            else:
                res[ind] = nR
                R -= 1
            ind -= 1
        return res

#  Time complexity: O(N), N is size of input
#  Space complexity: O(1), using pointers only
#  Take-away: using L and R pointers and populate res list from the end by
#  always picking the largest sqaured value