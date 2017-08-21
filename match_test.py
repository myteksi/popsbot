import unittest
import logics
import re


class MatchTest(unittest.TestCase):

    def test_match(self):
        self.assertEqual(True, logics.match(
            'i love you', ['i love you', ['i', 'you'], None]))
        self.assertEqual(True, logics.match(
            'i love you', ['i love you', ['i', 'you'], re.compile('i.*you', re.IGNORECASE)]))
        self.assertEqual(False, logics.match(
            'i love you', ['i love you', ['i', 'him'], re.compile('iyou', re.IGNORECASE)]))
