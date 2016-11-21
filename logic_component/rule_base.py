
class AbsractException(Exception):
    pass

class ContradictoryPremisesException(Exception):
    pass

class RuleBase:
    ''' Abstract base Class'''

    @classmethod
    def provable(cls, claim, premises):
        ''' True if the claim can be proven from the premises.'''
        raise AbstractException

    @classmethod
    def contradicts(cls, claim, premises):
        ''' True if the claim contradicts the premises.'''
        raise AbstractException

    @classmethod
    def evaluate(cls, claim, premises):
        ''' Return True if the claim is provable from the premises,
        False, if the claim contradicts the premises,
        and None otherwise.'''
        if cls.internalContradictions(cls, premises):
            raise ContradictoryPremisesException
        elif cls.provable(cls, claim, premises):
            return True
        elif cls.contradicts(cls, claim, premises):
            return False
        else:
            return None

    @classmethod
    def internalContradictions(cls, premises):
        ''' Return true if the premises contain contradictions.'''
        raise AbstractException

    @classmethod
    def optimalContradictions(cls, premises):
        ''' Return a list of all contradictions in the premises.

        Contradictions should be expressed such that removing any claim removes
        the contradiction.'''
        pass

    @classmethod
    def optimalSubsets(cls, premises):
        ''' Return a list of subsets of claims.

        These subsets must contain no contradictions, and it must be impossible
        to add another claim from claims to the subset without introducing a
        contradiction.'''
        pass
