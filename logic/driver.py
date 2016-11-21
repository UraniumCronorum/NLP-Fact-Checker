# driver.py

from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def fc_test():
    engine.reset()
    try:
        engine.activate('fc_syll')
    except:
        krb_traceback.print_exc()
        sys.exit(1)

def bc_test():
    engine.reset()
    try:

        engine.activate('bc_syll')
        with engine.prove_goal('bc_syll.all($S, $P)') as goalAll:
            for vars, plan in goalAll:
                print 'All that are', vars['S'], 'are', vars['P']

        with engine.prove_goal('bc_syll.some($S, $P)') as goalSome:
            # looking for "some elderly are mortal"
            for vars, plan in goalSome:
                print 'Some that are', vars['S'], 'are', vars['P']
    except:
        krb_traceback.print_exc()
        sys.exit(1)

if __name__=='__main__':
    print "Forward chaining:"
    fc_test()
    print "Backward chaining:"
    bc_test()
