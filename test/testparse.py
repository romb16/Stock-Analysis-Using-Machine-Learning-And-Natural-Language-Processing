import unittest
from parse import URLParser

class MyTestCase(unittest.TestCase):
    def test_parseurl(self):
        self.assertEqual(URLParser().parseurl(url), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
