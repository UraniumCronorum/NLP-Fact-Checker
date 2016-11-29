
import sys

import tagger

tgr = tagger.initialize_tagger()

for line in open(sys.argv[1]):
    tokens = tagger.tokenize(line)
    tags = tagger.get_tags(tgr, tokens)
    relation = tagger.extract_player_relation(tags)
    print relation

