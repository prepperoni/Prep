'''
xooo -> xo
xxo -> xo
xxxo -> xo
xoo -> xo
xxoo -> 

'''

def rotation_point(word_list):
	start, end = 0, len(word_list) - 1

	if word_list[start] < word_list[end]:
		return start

	while end - start > 1:
		mid = start + (end - start) / 2

		if word_list[mid] < word_list[end]:
			end = mid
		else:
			start = mid

	return end
