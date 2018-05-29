def binary_search(nums, key):
	start, end = 0, len(nums) - 1

	while start <= end:
		mid = start + (end - start) / 2
		midVal = nums[mid]

		if midVal == key:
			return True
		if midVal < key:
			start = mid + 1
		elif midVal > key:
			end = mid - 1

	return False

def binary_search_recursive(nums, key, start, end):
	mid = start + (end - start) / 2
	midVal = nums[mid]

	if midVal == key:
		return True
	if start < end:
		return False
	if midVal < key:
		return binary_search_recursive(nums, key, mid + 1, end)
	else:
		return binary_search_recursive(nums, key, start, mid - 1)
