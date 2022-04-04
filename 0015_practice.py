def threeSum(nums):
	if len(nums) < 3:
		return []
	indices = {}
	for i in range(len(nums)):
		if nums[i] in indices:
			indices[nums[i]].append(i)
		else:
			indices[nums[i]] = [i]
	print(indices)
	pass

print(threeSum([]))
print(threeSum([-1,0,1,2,-1,-4]))