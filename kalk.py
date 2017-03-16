import re

from functools import reduce


class Kalk:
    """A Kalkulator """

    @staticmethod
    def add(s):
        try:
            strings = re.split(',|\n', s)
            numbers = [int(n) for n in strings]
            negatives = [n for n in numbers if n < 0]

            if len(negatives) > 0:
                raise ValueError

            return reduce(lambda total, n: total + n,
                          map(lambda n: int(n), strings), 0)

        except ValueError:
            return 0
