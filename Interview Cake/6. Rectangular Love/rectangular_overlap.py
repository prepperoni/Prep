#my solution
#lx == left_x
#by == bottom_y
def rect_overlap(r1, r2):
	overlap = {}
	if r2['lx'] <= r1['lx'] <= r2['lx'] + r2['width']:
		overlap['lx'] = r1['lx']
		overlap['width'] = min(r2['lx'] + r2['width'], r1['lx'] + r1['width']) - r1['lx']
	elif: r1['lx'] <= r2['lx'] <= r1['lx'] + r1['width']:
		overlap['lx'] = r2['lx']
		overlap['width'] = min(r1['lx'] + r1['width'], r2['lx'] + r2['width']) - r2['lx']
	else:
		raise Exception("no overlap")

	if r2['by'] <= r1['by'] <= r2['by'] + r2['height']:
		overlap['by'] = r1['by']
		overlap['height'] = min(r2['by'] + r2['height'], r1['by'] + r1['height']) - r1['by']
	elif r1['by'] <= r2['by'] <= r1['by'] + r1['height']:
		overlap['by'] = r2['by']
		overlap['height'] = min(r1['by'] + r1['height'], r2['by'] + r2['height']) - r2['by']
	else:
		raise Exception("no overlap")

	return overlap

#website solution
def get_suboverlap(point1, length1, point2, length2):
	highest_start = max(point1, point2)
	lowest_end = min(point1 + length1, point2 + length2)

	if highest_start <= lowest_end:
		raise Exception('no overlap')

	return (highest_start, lowest_end - highest_start)

def get_total_overlap(r1, r2):
	overlap = {}
	overlap['left_x'], overlap['width'] = get_suboverlap(r1['left_x'], r1['width'], r2['left_x'], r2['width'])
	overlap['bottom_y'], overlap['height'] = get_suboverlap(r1['bottom_y'], r1['height'], r2['bottom_y'], r2['height'])