class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if max(nums) < 0:
            return max(nums)
        sums = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sums.append(sum)
        print(sums)

        currMin = sums[0]
        currMax = 0
        validMax = 0
        currAns = 0
        validAns = 0

        for i in range(1, len(sums)):
            if sums[i]<currMin:
                currMin = sums[i]
                validMax = 0
            elif validMax == 0:
                currMax = sums[i]
                validMax = 1
                if validAns and (currMax-currMin)>currAns:
                    currAns = currMax - currMin
                elif validAns == 0:
                    currAns = currMax - currMin
                    validAns = 1
            elif sums[i]>currMax:
                currMax = sums[i]
                if validAns and (currMax-currMin)>currAns:
                    currAns = currMax - currMin
                elif validAns == 0:
                    currAns = currMax - currMin
                    validAns = 1

        if validAns:
            sums.append(currAns)
        return (max(sums))