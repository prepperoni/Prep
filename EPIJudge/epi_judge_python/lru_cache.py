from sys import exit
from collections import OrderedDict

from test_framework import generic_test, test_utils
from test_framework.test_failure import TestFailure


class LruCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.d = OrderedDict()

    def lookup(self, isbn):
        if isbn in self.d:
            price = self.d.pop(isbn)
            self.d[isbn] = price
            return price
        else:
            return -1

    def insert(self, isbn, price):
        if isbn in self.d:
            self.lookup(isbn)
        else:
            if len(self.d) == self.cap:
                self.d.popitem(last=False)
            self.d[isbn] = price

    def erase(self, isbn):
        if isbn not in self.d:
            return False
        else:
            self.d.pop(isbn)
        return True

def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(generic_test.generic_test_main('lru_cache.tsv', run_test))
