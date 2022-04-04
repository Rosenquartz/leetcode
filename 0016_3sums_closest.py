class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Sort array 
        nums.sort()
        n = len(nums)

        # Use pointers for current array of closest values
        current_left = 0
        current_mid = 1
        current_right = n-1

        # Return empty set if array of three values is impossible
        if len(nums) < 3:
            return []

        # Use large difference that cannot be reached by constraints
        # (basically INF)
        closest_diff = 10000

        # Loop starting at left pointer pointing to first value
        for left in range(0,n-2):
            # Break out of loop if closest value (0) is achieved
            if closest_diff == 0:
                break

            # Method to avoid double checking left pointer
            if left > 0 and nums[left] == nums[left-1]:
                continue

            # Initialize mid and right pointers
            mid = left + 1
            right = n-1
            while (mid < right):
                current_diff = nums[left] + nums[mid] + nums[right] - target

                # If current_diff is 0, no need to keep checking
                if current_diff == 0:	
                    closest_diff = current_diff			
                    current_left = left
                    current_mid = mid
                    current_right = right
                    break

                # If new diff is better, update the pointers in the best array
                if abs(current_diff) < closest_diff:
                    closest_diff = abs(current_diff)
                    current_left = left
                    current_mid = mid
                    current_right = right

                # Check which pointer to move (mid to the right or right to the left)
                if abs(nums[left] + nums[mid+1] + nums[right] - target) < abs(nums[left] + nums[mid] + nums[right-1] - target):
                    mid = mid + 1
                else:
                    right = right - 1
                
        return(nums[current_left] + nums[current_mid] + nums[current_right])