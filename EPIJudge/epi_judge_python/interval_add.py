import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval1(disjoint_intervals, new_interval):
    res = []
    left_idx = None
    left_val = None
    for i, di in enumerate(disjoint_intervals):
        if new_interval.left <= di.right:
            left_val = min(new_interval.left, di.left)
            left_idx = i
            break
        res.append(di)

    if left_idx is None:
        res.append(new_interval)
        return res

    right_idx = None
    for j in range(left_idx, len(disjoint_intervals)):
        cur = disjoint_intervals[j]

        if new_interval.right < cur.left:
            res.append(Interval(left_val, new_interval.right))
            right_idx = j
            break
        elif new_interval.right <= cur.right:
            res.append(Interval(left_val, cur.right))
            right_idx = j + 1
            break

    if right_idx is None:
        res.append(Interval(left_val, new_interval.right))
        return res

    return res + disjoint_intervals[right_idx:]

#book solution
def add_interval(disjoint_intervals, new_interval):
    res = []
    i = 0

    while i < len(disjoint_intervals) and new_interval.left > disjoint_intervals[i].right:
        res.append(disjoint_intervals[i])
        i += 1

    if i < len(disjoint_intervals):
        left_val = min(new_interval.left, disjoint_intervals[i].left)
    
    while i < len(disjoint_intervals) and new_interval.right >= disjoint_intervals[i].left:
        new_interval = Interval(left_val, max(new_interval.right, disjoint_intervals[i].right))
        i += 1

    return res + [new_interval] + disjoint_intervals[i:]



@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
