
import rule_base

def table(claim, length = 8):
    out = [bool(int(x)) for x in bin(claim)[2:]]
    while len(out) < length:
        out.insert(0, False)
    return out

def negate(claim):
    return ~claim

class NumericalClaim(rule_base.RuleBase):

    @classmethod
    def provable(cls, claim, premises):
        claim = table(claim)
        premises = [table(premise) for premise in premises]

        # If it's possible for all premises to be true and the claim false,
        # the claim is not provable from the premises
        for i, entry in enumerate(claim):
            if all(premise[i] for premise in premises) and not entry:
                return False
        return True

    @classmethod
    def contradicts(cls, claim, premises):
        claim = table(claim)
        premises = [table(premise) for premise in premises]

        # If it's possible for all premises to be true when the claim is true,
        # there is no contradiction
        for i, entry in enumerate(claim):
            if all(premise[i] for premise in premises) and entry:
                return False
        return True

    @classmethod
    def internalContradictions(cls, premises):
        premises = [table(premise) for premise in premises]

        # If it's possible for all premises to be true, there is no contradiction
        for i in range(8):
            if all(premise[i] for premise in premises):
                return False
        return True

def evaluate(claim, premises):
    return NumericalClaim.evaluate(claim, premises)
