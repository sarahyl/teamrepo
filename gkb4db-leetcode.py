class Solution(object):
    def removeElement(self, nums, val):
        while True: 
            try:   # to avoid Value Error
                cval = nums.index(val)
            except: 
                break
            nums.pop(cval)
        return len(nums)