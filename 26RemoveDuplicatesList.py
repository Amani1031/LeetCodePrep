
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)
        while i < (len(nums) - 1):
            if nums[i + 1] == nums[i]:
                nums[i] = 101
                length -= 1
            i += 1
        nums.sort()
        return length


'''
Better solution:

public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
*Uses i as pointer and j as pointer. i tracks unique ones while j tracks all

'''