def threeSum(nums):
	if len(nums) < 3:
		return []
	indices = {}
	for i in range(len(nums)):
		if nums[i] in indices:
			indices[nums[i]].append(i)
		else:
			indices[nums[i]] = [i]

	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			third_value = -1 * (nums[i] + nums[j])
			print(i,j,indices[third_value])
	pass

print(threeSum([]))
print(threeSum([-1,0,1,2,-1,-4]))