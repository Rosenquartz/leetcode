def median (a,b,parity):
	m = len(a)
	n = len(b)
	if parity == 0:
		# Base case: both are now of length 1 or of length 2.
		if m == 1 and n == 1:
			return (a[0] + b[0]) // 2
		if m == 2 and n == 2:
			a.append(n[0])
			a.append(n[1])
			a.sort()
			return (a[1]+a[2]) / 2
		# Have to take average of two middle values
		# Two cases: both have an even number of values or an odd number of values.
		if m % 2 == 0:
			# First case: both have an even number of values.
			a_median = (a[m//2-1] + a[m//2]) // 2
			b_median = (b[n//2-1] + b[n//2]) // 2
			if a_median < b_median:
				return median(a[m:],b[:m],0)
			else:
				return median(a[:m],b[m:],0)
		else:
			a_median = a[m]
			b_median = b[m]
			if a_median < b_median:
				return median(a[m:],b[:m+1],0)
			else:
				return median(a[:m+1],b[m:],0)
		pass
	else:
		# Just have to find middle value.
		pass
print(median([1,3,5],[2,4,6],0))