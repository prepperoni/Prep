def examine_buildings_with_sunset(sequence):
	if not sequence:
		return []

	withView = [[sequence[0], 0]]

	for i in range(1, len(sequence)):
		while withView and withView[-1][0] <= sequence[i]:
			withView.pop()
		withView.append([sequence[i], i])

	return [x[1] for x in reversed(withView)]


def examine_buildings_with_sunset_wrapper(sequence):
	return examine_buildings_with_sunset(iter(sequence))


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
	exit(
		generic_test.generic_test_main('sunset_view.tsv',
									   examine_buildings_with_sunset))
