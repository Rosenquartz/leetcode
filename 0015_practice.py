def threeSum(nums):
	if len(nums) < 3:
		return []

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
	#print(values)
	#print(nums_compressed)

	'''
	lists = []
	for i in range(len(nums_compressed)):
		for j in range(i+1, len(nums_compressed)):
			third_value = -1 * (nums_compressed[i] + nums_compressed[j])
			print(i,j,third_value)
			if third_value in values:
				if values[third_value] > j:
					new_list = [nums_compressed[i],nums_compressed[j],third_value]
					new_list.sort()
					lists.append(new_list)
	return lists'''
	'''
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
	'''
print(threeSum([]))
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,0,0,0,0,0,0,0,0,0,0,0,0]))

# First iteration: too slow
# Duplicate values can be preprocessed by making a dictionary instead