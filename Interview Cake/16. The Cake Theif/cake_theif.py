def cake_theif(items, capacity):
	tracker = [0] * (capacity + 1)
	maxValue = 0

	for i in range(capacity + 1):
		if i == 0 or tracker[i] > 0:
			for item in items:
				weight, val = item
				if i + weight <= capacity:
					tracker[i + weight] = max(tracker[i + weight], tracker[i] + val)
					maxValue = max(maxValue, tracker[i] + val)

	return maxValue

items = [(7, 160), (3, 90), (2, 15)]
capacity = 20

print(cake_theif(items, capacity))