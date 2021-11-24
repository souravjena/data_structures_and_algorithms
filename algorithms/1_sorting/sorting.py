

# Insertion Sort CS50: https://www.youtube.com/watch?v=O0VbBkUvriI
def insertion_sort(arr):

	# Get element from the Unsorted Region
	for i_unsort in range(1, len(arr)):
		
		# Compare the element form the Unsorted Region
		# with elements in the Sorted Region till you find
		# its correct postion in the sorted region.
		i_sort = i_unsort - 1 	
		while ((arr[i_unsort] < arr[i_sort]) and (i_sort >= 0) ):
			# Swap
			temp = arr[i_unsort]
			arr[i_unsort] = arr[i_sort]
			arr[i_sort] = temp

			i_unsort = i_sort # Update index of unsorted element.
			i_sort -= 1		  # Move to the next element in the sorted region.
		
	return arr





# Selection Sort CS50: https://www.youtube.com/watch?v=3hH8kTHFw2A
'''
- Move the smallest element to its correct position after each iteration. {sorted region grows from left}
'''
def selection_sort(arr):
	len_arr = len(arr) - 1

	for start_unsort in range(len_arr):
		# Find the smallest element in the unsorted part
		
		min_ele = arr[start_unsort]
		min_idx = start_unsort

		for i in range(start_unsort, len_arr+1):
			if(arr[i] < min_ele):
				min_ele = arr[i]
				min_idx = i

		# Swap min with last element of the unsorted array
		temp = arr[start_unsort]
		arr[start_unsort] = arr[min_idx]
		arr[min_idx] = temp

	return arr





# Bubble Sort CS50: https://www.youtube.com/watch?v=RT-hUXUWQ2I
'''
- "Bubble" the largest element to its correct position after each iteration. 
'''
def bubble_sort(arr):

	'''
	- flag_swap is a way to optimize the code.
	- If there are no swaps in a pass that would mean the array is sorted.
	- So, we can directly return from there.
	'''
	flag_swap = False

	len_arr = len(arr)

	for i in range(len_arr - 1):
		flag_swap = False

		# Go through the unsorted region
		# "Bubble" the largest element to the end. {sorted region grows from right.}
		for j in range(1, len_arr - i):
			left = arr[j-1]
			right = arr[j]

			if(right < left):
				flag_swap = True

				temp = arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = temp

		# If is a single pass there was no swap that would mean
		# the array is sorted.
		if(flag_swap is False):
			return arr

	return arr




# Merge Sort CS50: https://www.youtube.com/watch?v=Ns7tGNbtvV4
# TC: nlogn, Space: n

# Helper Function for Merge Sort
def merge(sorted_arr_left, sorted_arr_right):
	sorted_arr = []

	l = 0
	r = 0
	len_left = len(sorted_arr_left)
	len_right = len(sorted_arr_right)

	while ((l < len_left) and (r < len_right)):

		if(sorted_arr_left[l] < sorted_arr_right[r]):
			sorted_arr.append(sorted_arr_left[l])
			l += 1
		else:
			sorted_arr.append(sorted_arr_right[r])
			r += 1

	else:
		if(l == len_left and r < len_right):
			sorted_arr = sorted_arr + sorted_arr_right[r:]
		elif(r == len_right and l < len_left):
			sorted_arr = sorted_arr + sorted_arr_left[l:]

	return sorted_arr


# Merge Sort Function
def merge_sort(arr):

	len_arr = len(arr)

	# Base Case
	if(len_arr == 1):
		# sub-array is sorted, so return
		return arr

	# Recursive Case
	mid_idx = (len_arr//2)

	sorted_arr_left = merge_sort(arr[:mid_idx])
	sorted_arr_right = merge_sort(arr[mid_idx:])

	# Current Problem
	sorted_arr = merge(sorted_arr_left, sorted_arr_right)

	return sorted_arr




# Quick Sort Computerphile: https://www.youtube.com/watch?v=XE4VP_8Y0BU
# Cleanest QuickSort Code: https://www.youtube.com/watch?v=kFeXwkgnQ9U -> NOTE: Not doing in-place sorting here.

'''
1. Select a Pivot (right most element).
2. Compare rest of the elements with the pivot.
3. At the end of this comparision, elements smaller than the pivot should be on left
   and elements greater than pivot should be on its right.

<This will move the pivot point to its correct position in the array>

4. Repeat 1 for left and right part.
'''

# Avg. TC: nlogn
# Worst TC: n^2
# Stable: No

# **Non-in-place** solution of Quick Sort
def quick_sort(arr):

	len_arr = len(arr)

	# 1. Base Case
	if(len_arr <= 1):
		# the sub-array is already sorted
		return arr


	# 2. Recursive Case
	pivot = arr.pop() 	# Choose right most element as pivot

	arr_smaller = []
	arr_greater = []

	for item in arr:
		if(item < pivot):
			arr_smaller.append(item)
		else:
			arr_greater.append(item)

	sorted_arr_left = quick_sort(arr_smaller)
	sorted_arr_right = quick_sort(arr_greater)


	# 3. Current Problem
	sorted_arr = sorted_arr_left + [pivot] + sorted_arr_right

	return sorted_arr







def main():
	unsorted_arr = [2, 2, 2, 1, 3, 5, 4, 6]
	sorted_arr = quick_sort(unsorted_arr)

	print(sorted_arr)



if __name__ == '__main__':
	main()