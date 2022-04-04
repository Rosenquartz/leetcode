class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        saveCounter = 0
        moveCounter = 1
        if len(nums)==0:
            return 0
        while(1):
            if moveCounter >= len(nums):
                break
            if nums[moveCounter] == nums[saveCounter]:
                moveCounter += 1
            else:
                saveCounter += 1
                nums[saveCounter]=nums[moveCounter]
                moveCounter += 1
        return saveCounter + 1
        