import unittest

from kalk import Kalk


class KalkTest(unittest.TestCase):
    def testOnEmptyString(self):
        self.assertEqual(0, Kalk.add(""))

    def testASingleNumber(self):
        self.assertEqual(42, Kalk.add('42'))

    def testTwoNumbers(self):
        self.assertEqual(42, Kalk.add('40,2'))

    def testManyNumbers(self):
        self.assertEqual(42, Kalk.add('20,20,2'))

    def testWithSpaces(self):
        self.assertEqual(42, Kalk.add('20 , 20,  2'))

    def testWithNewlines(self):
        self.assertEqual(42, Kalk.add('20 \n 20\n  2'))

    def testWithCommasNewlines(self):
        self.assertEqual(42, Kalk.add('20 , 20\n  2'))

    def testWithNegatives(self):
        self.assertRaisesRegex(ValueError, "Negative numbers are not allowed: (-\d+(, )?)+",
                               Kalk.add, '20, -20, -10, 2')

if __name__ == '__main__':
    unittest.main()
