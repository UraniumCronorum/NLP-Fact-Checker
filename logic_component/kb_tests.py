
import unittest
from knowledge_base import *
from rulebases.numericalTT import NumericalClaim

class SourceTest(unittest.TestCase):

    def setUp(self):
        self.db = KnowledgeBase(NumericalClaim)
        self.sources = [Source(str(i)) for i in range(3)]

    def testTruthRanking(self):
        self.db.addKnown(self.sources[0],5)   # 0101: q
        self.db.addKnown(self.sources[0], 13)  # 1101: p->q

        self.db.addClaim(self.sources[1], 5)  # 0101: q
        self.db.addClaim(self.sources[1], 13)  # 1101: p->q
        self.assertEqual(self.db.truthRanking(self.sources[1]),
                         TruthRanking(2, 0, 0))
        self.assertEqual(self.db.reliability(self.sources[1]),
                         1)

        self.db.addClaim(self.sources[2], 5)  # 0101: q
        self.db.addClaim(self.sources[2], 10)  # 1010: ~q
        self.db.addClaim(self.sources[2], 11)  # 1011: q->p
        self.db.addClaim(self.sources[2], 14)  # 1110: p->~q
        self.assertEqual(self.db.truthRanking(self.sources[2]),
                         TruthRanking(1, 1, 2))
        self.assertEqual(self.db.reliability(self.sources[2]),
                         .5)
        
    def testContradictions(self):
        self.db.addClaim(self.sources[1], 5)  # 0101: q
        self.db.addClaim(self.sources[1], 13)  # 1101: p->q

        self.db.addClaim(self.sources[2], 5)  # 0101: q
        self.db.addClaim(self.sources[2], 10)  # 1010: ~q
        self.db.addClaim(self.sources[2], 11)  # 1011: q->p
        self.db.addClaim(self.sources[2], 14)  # 1110: p->~q

        self.assertFalse(self.db.contradictsSelf(self.sources[1]))
        self.assertTrue(self.db.contradictsSelf(self.sources[2]))

class KnowledgeTest(unittest.TestCase):

    def setUp(self):
        self.db = KnowledgeBase(NumericalClaim)
        self.known = Source('known')
        self.other = Source('s1')

    def testAdd(self):
        self.db.addKnown(self.known, 13)  # 1101: p->q
        self.db.addClaim(self.other, 3)   # 0011: p
        self.db.addClaim(self.other, 10)  # 1010: ~q

        with self.assertRaises(KnownException):
            self.db.addKnown(self.known, 2) # 0010: ~(p->q)

        self.assertTrue(self.db.trueOrFalse(13)) # 1101: p->q
        self.assertIsNone(self.db.trueOrFalse(3)) # 0011: p
        self.assertFalse(self.db.trueOrFalse(2)) # 0010: ~(p->q)

        self.assertTrue(self.db.evaluate(self.db.claimsBySource(self.other),
                                          2)) # 0010: ~(p->q)

if __name__ == '__main__':
    unittest.main()
