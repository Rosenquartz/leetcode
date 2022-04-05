class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_dict = {}
        nums.sort()

        n = len(nums)
        if n < 4:
            return []

        for i in range(n):
            if nums[i] in nums_dict:
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]

        return_array = []

        for i in range(n-3):
            threesumoutput = self.threeSum(nums[i+1:],target-nums[i])
            if threesumoutput != []:
                for j in threesumoutput:
                    k = [nums[i]]
                    k += j
                    if k not in return_array:
                        return_array.append(k)
        return return_array
            
    # Use three sum solution:
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        indices = {}
        for i in range(len(nums)):
            if nums[i] in indices:
                indices[nums[i]].append(i)
            else:
                indices[nums[i]] = [i]

        lists = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                third_value = target - (nums[i] + nums[j])
                if third_value in indices:
                    if max(indices[third_value]) > j:
                        new_list = [nums[i], nums[j], third_value]
                        new_list.sort()
                        if new_list in lists:
                            continue
                        else:
                            lists.append(new_list)
        return lists