#Sarah Liu 
#syl3mb

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        unique = 1
        
        while unique < len(nums):
            if nums[current] == nums[unique]:
                unique+=1
            else:
                current+=1
                nums[current] = nums[unique]
                unique+=1
        return current + 1