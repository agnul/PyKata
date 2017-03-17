import re

from functools import reduce


class Kalk:
    """A Kalkulator """

    @staticmethod
    def add(s):
        if not s:
            return 0

        strings = re.split(get_delimiters(s), s)

        numbers = [parse_number(n) for n in strings]
        negatives = [n for n in numbers if n < 0]

        if len(negatives) > 0:
            raise ValueError('Negative numbers are not allowed: {}'.format(', '.join(map(str, negatives))))

        return reduce(lambda total, n: total + n, numbers, 0)


def get_delimiters(s):
    delimiters = [",", "\n"]

    custom = find_between(s, "//", "\n")

    delimiters.append(custom)

    return '({})+'.format('|'.join(delimiters))


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def parse_number(s):
    try:
        return int(s)
    except ValueError:
        return 0
