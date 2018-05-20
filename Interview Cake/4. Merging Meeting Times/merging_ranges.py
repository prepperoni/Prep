def merge_ranges(meetings):
	meetings.sort()
	res = []
	rangeStart, rangeEnd = meetings[0]

	for i in range(1, len(meetings)):
		if meetings[i][0] <= rangeEnd:
			rangeEnd = max(rangeEnd, meetings[i][1])
		else:
			res.append([rangeStart, rangeEnd])
			rangeStart, rangeEnd = meetings[i]

	res.append([rangeStart, rangeEnd])
	return res