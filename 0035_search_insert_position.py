class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 1
        if len(nums)==1:
            if target>nums[0]: return 1
            else: return 0
        middle = len(nums)//2
        left = nums[0:middle]
        right = nums[middle:len(nums)]
        if target>nums[middle]:
            return len(left)+self.searchInsert(right,target)
        else:
            return self.searchInsert(left,target)