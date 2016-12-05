
import sys
import re

import nltk

doc = open(sys.argv[1]).read()

sentences = nltk.sent_tokenize(doc)
tok = map(lambda sentence: nltk.word_tokenize(sentence), sentences)
tagged = map(lambda sentence: nltk.pos_tag(sentence), tok)
chunked = nltk.ne_chunk_sents(tagged)

IN = re.compile(r'.*\bin\b(?!\b.+ing\b)')
AT = re.compile(r'at')

class doc:
    def __init__(self, chunk):
        self.headline=['']
        self.text=chunk

#semi = nltk.sem.relextract.tree2semi_rel(chunked)
#print semi
#reldicts = nltk.sem.relextract.semi_rel2reldict(semi)
#for reldict in reldicts:
#    for k, v in sorted(reldict.items()):
#        print k + ' => ' + v
#    print '*' * 20

#print nltk.sem.relextract.extract_rels('PERSON', 'ORGANIZATION', chunked, pattern = IN)

for chunk in chunked:
    #print nltk.sem.relextract.extract_rels('PERSON', 'GPE', chunk, pattern = IN)
    print chunk
    semi = nltk.sem.relextract.tree2semi_rel(chunk)
    for s in semi: print s
    #for s, tree in semi:
    #    print 's=' + str(s)
    #    print 'tree=' + str(tree)
    reldicts = nltk.sem.relextract.semi_rel2reldict(semi)
    for reldict in reldicts:
        for k, v in sorted(reldict.items()):
            print k + ' => ' + v
    print nltk.sem.relextract.extract_rels('PERSON', 'ORGANIZATION', doc(chunk), corpus='ieer', pattern = AT)
    print '******'

