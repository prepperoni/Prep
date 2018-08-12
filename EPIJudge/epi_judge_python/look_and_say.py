from test_framework import generic_test
'''

1
11
21
1211
111221

'''

def look_and_say(n):
    def next_seq(s):
        seq = []
        count = 1
        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != s[i-1]:
                seq += [str(count), s[i - 1]]
                count = 1
            else:
                count += 1
        return seq

    res = ['1']
    for _ in range(n - 1):
        res = next_seq(res)

    return ''.join(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
