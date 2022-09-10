from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            pivot = i;
            total = sum(nums[i+1:])
            if total == sum(nums[:i]):
                return pivot
        return -1

'''
My solution is too complicated.
Any time there is a "step through every index" to find a sum, use a "stairs" concept -- no need to calculate
the sum from scratch every time."

This would've been great to use "for i, x in enumerate(nums)" so you have both index and value
'''