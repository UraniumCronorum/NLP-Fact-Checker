
""" This module defines the database used for associating logical claims with their sources and truth values."""

from collections import namedtuple
import numericalTT

Claim = namedtuple('Claim', 'representation source')

class KnownException(Exception):
    pass

class Source:

    def __init__(self, name, a_priori = False):
        self.name = name
        self.a_priori = a_priori

class KnowledgeBase:
    
    def __init__(self, ruleBase):
        self.claims = set()
        self.base = ruleBase

    # Modify database
    def addClaim(self, source, claim):
        """ Add a new claim to the database"""
        if source.a_priori:
            if self.trueOrFalse(claim) is False:
                raise KnownException('Claim added as "known" raises contradiction with other known facts')
            self.claims |= {Claim(claim, source)}
        else:
            self.claims |= {Claim(claim, source)}

    # Extract information
    def sources(self):
        """ Return all the sources in the database"""
        out = []
        for claim in self.claims:
            if claim.source not in out:
                out += claim.source
        return out

    def knowns(self):
        """ Return all claims given as True"""
        out = [claim for claim in self.claims
               if claim.source.a_priori]
        return out

    def claimsBySource(self, source):
        """ Return all claims made by a certain source"""
        out = [claim for claim in self.claims
               if claim.source == source]
        return out

    # Apply rules
    def evaluate(self, knowns, claim):
        return self.base.evaluate(claim,
                                  [known.representation for known in knowns])

    def trueOrFalse(self, claim):
        return self.evaluate(self.knowns(), claim)

    # output
    def __str__(self):
        pass

##known_facts = Source('Known Facts', True)
##other_source = Source('definitelynotclickbait.com')
##
##db = KnowledgeBase()
##
##db.addClaim(known_facts, 'These are not small hands')
##db.addClaim(other_source, 'Elvis is not dead')
