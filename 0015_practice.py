def threeSum(nums):
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
			third_value = -1 * (nums[i] + nums[j])
			if third_value in indices:
				if max(indices[third_value]) > j:
					#print(i,nums[i],j,nums[j],third_value)
					new_list = [nums[i], nums[j], third_value]
					new_list.sort()
					if new_list in lists:
						continue
					else:
						lists.append(new_list)
	return lists

print(threeSum([]))
print(threeSum([-1,0,1,2,-1,-4]))

# First iteration: too slow
# Duplicate values can be preprocessed by making a dictionary instead