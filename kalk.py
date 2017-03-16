import re

from functools import reduce


class Kalk:
    """A Kalkulator """

    @staticmethod
    def add(s):
        if not s:
            return 0

        strings = re.split(',|\n', s)
        numbers = [int(n) for n in strings]
        negatives = [n for n in numbers if n < 0]

        if len(negatives) > 0:
            raise ValueError('Negative numbers are not allowed: {}'.format(', '.join(map(str, negatives))))

        return reduce(lambda total, n: total + n,
                      map(lambda n: int(n), strings), 0)
