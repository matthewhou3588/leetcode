class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        
        if length == 0 or length == 1:
            return length

        
        i = 0
        j = 1
        
        while j < length:            
            while nums[i] == nums[j]:
                j += 1
                if j == length:
                    break
            if j < length:
                nums[i+1] = nums[j]
                i += 1
                j += 1
            else:
                break
        
        return i+1
        
