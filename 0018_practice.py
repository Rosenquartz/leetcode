def foursum(nums, target):
	nums_dict = {}
	nums.sort()
	print(nums)
	n = len(nums)
	if n < 4:
		return []

	for i in range(n):
		if nums[i] in nums_dict:
			nums_dict[nums[i]].append(i)
		else:
			nums_dict[nums[i]] = [i]
	
	return_array = []

	for left in range(n-3):
		mid, right = left+1, n-1
		while (mid < right):
			print(left,mid,right, ' ... ', nums[left],nums[mid], nums[right])
			remainder = target - nums[left] - nums[mid] - nums[right]
			if remainder in nums_dict:
				appended = 0
				remainder_array = nums_dict[remainder]
				print(remainder,remainder_array,left,mid,right)
				for i in remainder_array:
					if mid < i and i < right:
						return_array.append([nums[left],nums[mid],nums[i],nums[right]])
						appended = 1
						print('found ittt')
						break
				#print('-----------',left,mid,right)
				if appended:
					mid = mid + 1
					print('appended, ', remainder)
					# if remainder<0:
					# 	mid = mid + 1
					# else:
					# 	right = right - 1
					#print('-----------',left,mid,right)
					continue
			
			if remainder < 0:
				mid = mid + 1
			else:
				right = right - 1
	return return_array
print(foursum([1,0,-1,0,-2,2],0))