
import rule_base
from syll.driver import engine
from pyke.knowledge_engine import CanNotProve

class SyllClaim(rule_base.RuleBase):

    opposites = {'all':'notAll','no':'some','some':'no',
                 'notAll':'all'}

    def __init__(self, quantifier, subject, predicate):
        self.q= quantifier
        self.s= subject
        self.p= predicate

    def state(self):
        engine.assert_('syll', self.q, (self.s, self.p))

    @classmethod
    def provable(cls, claim, premises):
        engine.reset()
        for premise in premises:
            premise.state()
        goal = 'syll.'+claim.q+'('+claim.s+','+claim.p+')'
        try:
            engine.prove_1_goal(goal)
            return True
        except CanNotProve:
            return False

    @classmethod
    def contradicts(cls, claim, premises):
        engine.reset()
        for premise in premises:
            premise.state()
        goal = 'syll.'+cls.opposites[claim.q]+'('+claim.s+','+claim.p+')'
        try:
            engine.prove_1_goal(goal)
            return True
        except CanNotProve:
            return False

    @classmethod
    def internalContradictions(cls, premises):
        for p in premises:
            if cls.contradicts(p, premises):
                return True
        else:
            return False

adorableCats = SyllClaim('all', 'cats', 'adorable')
nonAdorableCats = SyllClaim('notAll', 'cats', 'adorable')
adorableDogs = SyllClaim('all', 'dogs', 'adorable')

print SyllClaim.provable(adorableCats, [adorableCats])
print SyllClaim.contradicts(adorableCats, [adorableCats])

print SyllClaim.provable(nonAdorableCats, [adorableCats])
print SyllClaim.contradicts(nonAdorableCats, [adorableCats])

print SyllClaim.internalContradictions([adorableCats])
print SyllClaim.internalContradictions([adorableCats, nonAdorableCats])
