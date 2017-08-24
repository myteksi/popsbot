import unittest
import logics


class PrepareTest(unittest.TestCase):

    def test_prepare(self):
        self.assertEqual('hahahttp://shithoho',
                         logics.prepare('haha<http://shit>hoho'))
        self.assertEqual('hahashithoho',
                         logics.prepare('haha<mailto:shit>hoho'))
        self.assertEqual('hahahttp://whocares, hohohttps://icare',
                         logics.prepare('haha<http://whocares>, hoho<https://icare>'))
        self.assertEqual('hahahttp://whocares, hoho<https://icare',
                         logics.prepare('haha<http://whocares>, hoho<https://icare'))
