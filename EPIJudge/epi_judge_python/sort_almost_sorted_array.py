from test_framework import generic_test


def sort_approximately_sorted_array(sequence, k):
    h = []
    res = []

    for i in range(min(k, len(sequence))):
        heappush(h, sequence[i])

    for i in range(k, len(sequence)):
        heappush(h, sequence[i])
        res.append(heappop(h))

    while h:
        res.append(heappop(h))

    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
