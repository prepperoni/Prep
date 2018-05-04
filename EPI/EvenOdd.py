def evenOdd(arr):
	evenIdx, oddIdx = 0, len(arr) - 1

	while evenIdx < oddIdx:
		if evenIdx % 2 == 0:
			evenIdx += 1
		else:
			arr[evenIdx], arr[oddIdx] = arr[oddIdx], arr[evenIdx]
			oddIdx -= 1