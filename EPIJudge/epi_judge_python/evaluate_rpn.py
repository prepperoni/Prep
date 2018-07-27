from test_framework import generic_test

#5, 6, /, 7, *
def evaluate(expression):
    items = expression.split(',')
    stk = []

    for i, k in enumerate(items):
        if k in '+-*/':
            second, first = stk.pop(), stk.pop()

            if k == '-':
                stk.append(first - second)
            elif k == '+':
                stk.append(first + second)
            elif k == '*':
                stk.append(first * second)
            elif k == '/':
                stk.append(first // second)
        else:
            stk.append(int(k))

    return stk.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
