# driver.py

from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def test():
    engine.reset()
    try:
        engine.assert_('sports', 'weighs', ('p1', 100))
        engine.assert_('sports', 'weighs', ('p2', 200))
        engine.activate('bc_sports')
        with engine.prove_goal('bc_sports.heavier($h, $l)') as goal:
            for vars, plan in goal:
                print vars
        print engine.prove_1_goal('bc_sports.heavier(p2, p1)')
        #print engine.prove_1_goal('bc_sports.heavier(p1, p2)')
    except:
        krb_traceback.print_exc()
        sys.exit(1)

if __name__=='__main__':
    test()

