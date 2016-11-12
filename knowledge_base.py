
from collections import namedtuple

Claim = namedtuple('Claim', 'pyke source TorF')

class Source:

    def __init__(self, name, a_priori = False):
        self.name = name
        self.a_priori = a_priori

class KnowledgeBase:
    
    def __init__(self):
        self.claims = set()

    def addClaim(self, source, claim):
        if source.a_priori:
            if self.trueOrFalse(claim) is False:
                raise Exception('Claim assumed a_priori raises contradiction with known facts')
            self.claims |= {Claim(claim, source, True)}
        else:
            self.claims |= {Claim(claim, source, self.trueOrFalse(claim))}

    def trueOrFalse(self, claim):
        return None

known_facts = Source('Known Facts', True)
other_source = Source('definitelynotclickbait.com')

db = KnowledgeBase()

db.addClaim(known_facts, 'These are not small hands')
db.addClaim(other_source, 'Elvis is not dead')

print db.claims
