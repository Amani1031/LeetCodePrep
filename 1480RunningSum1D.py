from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final = []
        for x in range(len(nums)):
            ans = self.addr(nums, 0, x)
            final.append(ans)
        return final

    def addr(self, nums: List[int], result: int, index: int) -> int:
        if index == 0:
            return result + nums[index]
        else:
            return self.addr(nums, result + nums[index], index - 1)

'''
No need for complicated recursion. Lists can be ammended so ammend each index to hold the ith + i-1 th value.
'''