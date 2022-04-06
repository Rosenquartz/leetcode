def next(array):
	n = len(array)

	# Case where last two numbers just swap.
	if array[n-2] < array[n-1]:
		temp = array[n-1]
		array[n-1] = array[n-2]
		array[n-2] = temp
		return array

	# If not, find the end of increasing numbers starting from the right
	end = n-1
	for i in range(n-2, -1, -1):
		if array[i] >= array[i+1]:
			end = i
		else:
			break
	if end == 0:
		#print('end is zero')
		reverse(array,0,n-1)
	else:
		#print('end is ', end)
		reverse(array,end,n-1)
		insert(array,end-1)
	return array

def reverse(array, left, right):
	while (left < right):
		temp = array[left]
		array[left] = array[right]
		array[right] = temp
		left += 1
		right -= 1

def insert(array, insertion):
	insert_this = array[insertion]
	i = insertion + 1
	while (i < len(array)):
		if array[insertion] < array[i]:
			array[insertion] = array[i]
			array[i] = insert_this
			break
		i += 1

	# for i in range(insertion+1, len(array)):
	# 	print(i)
	# 	if array[insertion] > array[i] and array[insertion] < array[i+1]:
	# 		for j in range(insertion,i):
	# 			array[j] = array[j+1]
	# 		array[i] = insert_this
	# 		break

print(next([2,3,2,1]))
#----