class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        saveCounter = 0
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[saveCounter] = nums[i]
                saveCounter += 1
        return saveCounter