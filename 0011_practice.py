def area(height):
	n = len(height)
	a = 0
	b = n - 1
	current_max = min(height[a],height[b]) * (n-1)
	# Idea: reduce width of container by exactly one per iteration.
	while (a < b):
		print(a,b)
		new_area_one = min(height[a], height[b-1]) * (b-a-1)
		new_area_two = min(height[a+1], height[b]) * (b-a-1)

		# Replace maximum if necessary
		if max(new_area_one,  new_area_two) > current_max:
			current_max = max(new_area_one,  new_area_two)
			if new_area_one > new_area_two:
				b = b - 1
			else:
				a = a + 1
		# Else just update a and b
		else:
			if height[a] > height[b]:
				b = b - 1
			else:
				a = a + 1

	return current_max


print(area([1,3,2,5,25,24,5]))