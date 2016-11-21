
import rule_base
from logic.driver import engine
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

    def internalContradictions(cls, premises):
        for p in premises:
            if cls.contradicts(p, premises):
                return True
        else:
            return False

adorableCats = SyllClaim('all', 'cats', 'adorable')
nonAdorableCats = SyllClaim('notAll', 'cats', 'adorable')
adorableDogs = SyllClaim('all', 'dogs', 'adorable')

print adorableCats.provable(adorableCats, [adorableCats])
print adorableCats.contradicts(adorableCats, [adorableCats])

print nonAdorableCats.provable(nonAdorableCats, [adorableCats])
print nonAdorableCats.contradicts(nonAdorableCats, [adorableCats])

print adorableCats.internalContradictions([adorableCats])
print adorableCats.internalContradictions([adorableCats, nonAdorableCats])
