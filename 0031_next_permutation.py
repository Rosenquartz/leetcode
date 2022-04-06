class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        array = nums
        n = len(array)

        # Three steps:
        # First, check if the last two values can just be swapped.
        # Otherwise, find the largest subarray of descending values (from the right).

        # Case where last two numbers just swap.
        if array[n-2] < array[n-1]:
            temp = array[n-1]
            array[n-1] = array[n-2]
            array[n-2] = temp
            return array

        # If not, find the largest subarray of ascending values (from the right).
        end = n-1
        for i in range(n-2, -1, -1):
            if array[i] >= array[i+1]:
                end = i
            else:
                break
        if end == 0:
            # If whole array, just reverse the list.
            self.reverse(array,0,n-1)
        else:
            # Otherwise, reverse the subarray to the right, and put the new value accordingly,
            # where the new value is the value to the immediate left of the largest subarray.
            # For example: in [2,3,5,4,1], the largest subarray is [5,4,1]. The new value is 3.
            # -> [2,3,5,4,1]
            # -> (sort largest descending subarray from the right) [2,3,1,4,5]
            # -> (insert 3 and replace with next value) [2,4,1,3,5]
            self.reverse(array,end,n-1)
            self.insert(array,end-1)
        return array

    def reverse(self, array, left, right):
        # Method that reverses subset of array
        while (left < right):
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1

    def insert(self, array, insertion):
        # Method that inserts a value in its (sorted) place in the subarray to its right.
        # Assumes that the subarray to its right is sorted in ascending order.
        insert_this = array[insertion]
        i = insertion + 1
        while (i < len(array)):
            if array[insertion] < array[i]:
                array[insertion] = array[i]
                array[i] = insert_this
                break
            i += 1