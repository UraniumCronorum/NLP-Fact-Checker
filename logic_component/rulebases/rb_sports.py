import rule_base
from sports.driver import engine
from pyke.knowledge_engine import CanNotProve

class SportsClaim(rule_base.RuleBase):

    def __init__(self, relation, args):
        self.relation = relation
        self.args = args

    def state(self):
        engine.assert_('sports', self.relation, self.args)

    @staticmethod
    def strArg(arg):
        return str(arg) if not type(arg) == str else arg

    @classmethod
    def strArgs(cls, *args):
        out = '('
        for arg in args:
            out += cls.strArg(arg)
            out += ','
        return out[:-1] + ')'

    valueClaims = ['plays_for', 'height', 'weight', 'age']

    def disproveValue(self):
        goal = 'bc_sports.'+self.relation+'('+self.strArg(self.args[0])+',$val)'
        with engine.prove_goal(goal) as g:
            for vars, plan in g:
                print 'vars = ' + str(vars)
                print 'plan = ' + str(plan)
                # should be at most one
                if vars['val'] != self.args[1]:
                    return True
                return False

    orderClaims = ['heavier', 'taller', 'older']
    def disproveOrder(self):
        goal = 'bc_sports.'+self.relation+self.strArgs(self.args[1],self.args[0])
        try:
            engine.prove_1_goal(goal)
            return True
        except CanNotProve:
            return False

    ## implementation of abstract class

    @classmethod
    def provable(cls, claim, premises):
        engine.reset()
        engine.activate('bc_sports')

        for premise in premises:
            premise.state()
        goal = 'bc_sports.'+claim.relation+cls.strArgs(*claim.args)
        print goal
        try:
            engine.prove_1_goal(goal)
            return True
        except CanNotProve:
            return False

    @classmethod
    def contradicts(cls, claim, premises):
        engine.reset()
        engine.activate('bc_sports')

        for premise in premises:
            premise.state()
        if claim.relation in cls.orderClaims:
            return claim.disproveOrder()
        elif claim.relation in cls.valueClaims:
            return claim.disproveValue()
        else:
            raise Exception('relation '+claim.relation+' not recognized.')

    @classmethod
    def internalContradictions(cls, premises):
        for p in premises:
            if cls.contradicts(p, premises):
                return True
        else:
            return False

if __name__=='__main__':
    weightClaims = [SportsClaim('weight', ('P1', 100)),
                    SportsClaim('weight', ('P2', 200))]

    print SportsClaim.provable(SportsClaim('heavier', ('P2','P1')),
                               weightClaims)
    print SportsClaim.contradicts(SportsClaim('heavier', ('P1','P2')),
                                  weightClaims)
