def closest(nums, target):
	nums.sort()
	n = len(nums)
	current_left = 0
	current_mid = 1
	current_right = n-1
	if len(nums) < 3:
		return []
	closest_diff = 10000
	for left in range(0,n-2):
		if closest_diff == 0:
			break
		if left > 0 and nums[left] == nums[left-1]:
			continue
		mid = left + 1
		right = n-1
		while (mid < right):
			current_diff = nums[left] + nums[mid] + nums[right] - target
			if current_diff == 0:	
				closest_diff = current_diff			
				current_left = left
				current_mid = mid
				current_right = right
				break
			if abs(current_diff) < closest_diff:
				closest_diff = abs(current_diff)
				current_left = left
				current_mid = mid
				current_right = right
			if abs(nums[left] + nums[mid+1] + nums[right] - target) < abs(nums[left] + nums[mid] + nums[right-1] - target):
				mid = mid + 1
			else:
				right = right - 1
	return([nums[current_left],nums[current_mid],nums[current_right]])
print(closest([-1,2,1,-4],1))