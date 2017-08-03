import unittest
import logics


class PrepareTest(unittest.TestCase):

    def test_prepare(self):
        self.assertEqual('hahahttp://shithoho',
                         logics.prepare('haha<http://shit>hoho'))
        self.assertEqual('hahashithoho',
                         logics.prepare('haha<mailto:shit>hoho'))
