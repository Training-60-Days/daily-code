27 - Remove Element
# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0 # the pointer that has the updated result
        
        # fast is the pointer that checks if next item should be excluded
        for fast in range(len(nums)):
            # we should include the item, slow pointer should be updated
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

#  Time complexity: O(N), N is size of input
#  Space complexity: O(1), using pointers only
#  Take-away: Be very careful about role of the fast pointer