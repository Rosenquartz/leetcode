class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        # Compress values into at most three of each, and
        # make a dictionary for O(1) look up time.
        values = {}
        nums_compressed = []
        counter = 0
        for i in range(len(nums)):
            if nums[i] in values:
                if len(values[nums[i]]) < 3:
                    values[nums[i]].append(counter)
                    nums_compressed.append(nums[i])
                    counter += 1
            else:
                values[nums[i]] = [counter]
                nums_compressed.append(nums[i])
                counter += 1

        # Iterate through two pointers starting from (0,1),
        # with right pointer always greater than left pointer.
        # If additive inverse of their sum is in the 
        # dictionary and has an index greater than the right 
        # pointer, then append it in the return list.
        lists = []
        for i in range(len(nums_compressed)):
            for j in range(i+1, len(nums_compressed)):
                third_value = -1 * (nums_compressed[i] + nums_compressed[j])
                #print(i,j,third_value)
                if third_value in values:
                    if max(values[third_value]) > j:
                        new_list = [nums_compressed[i],nums_compressed[j],third_value]
                        new_list.sort()
                        if new_list not in lists:
                            lists.append(new_list)
        return lists