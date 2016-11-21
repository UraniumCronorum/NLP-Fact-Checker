
import unittest
from knowledge_base import *
from numericalTT import NumericalClaim

class SourceTest(unittest.TestCase):
    pass

class KnowledgeTest(unittest.TestCase):

    def setUp(self):
        self.db = KnowledgeBase(NumericalClaim)
        self.known = Source('known', True)
        self.other = Source('s1')

    def testAdd(self):
        self.db.addClaim(self.known, 13)  # 1101: p->q
        self.db.addClaim(self.other, 3)   # 0011: p
        self.db.addClaim(self.other, 10)  # 1010: ~q

        with self.assertRaises(Exception):
            self.db.addClaim(self.known, 2) # 0010: ~(p->q)

        self.assertTrue(self.db.trueOrFalse(13)) # 1101: p->q
        self.assertIsNone(self.db.trueOrFalse(3)) # 0011: p
        self.assertFalse(self.db.trueOrFalse(2)) # 0010: ~(p->q)

        self.assertTrue(self.db.evaluate(self.db.claimsBySource(self.other),
                                          2)) # 0010: ~(p->q)

if __name__ == '__main__':
    unittest.main()
