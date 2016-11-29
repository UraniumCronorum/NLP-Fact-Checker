import re
import sys

from nltk import pos_tag, word_tokenize
from nltk.tag import StanfordNERTagger

def merge_tags(pos, ner):
    pos_dict = dict(pos)
    new_tags = []
    for tok, tag in ner:
        if (tag == 'O' and tok in pos_dict) or tok in ['of', 'the']:
            new_tags.append((tok, pos_dict[tok]))
        else:
            new_tags.append((tok, tag))
    prev_tag = ''
    prev_tok = ''
    merged_tags = []
    for tok, tag in new_tags:
        if tag == prev_tag and tag in ['PERSON', 'ORGANIZATION']:
            prev_tok += ' ' + tok
            prev_tag = tag
        else:
            merged_tags.append((prev_tag, prev_tok))
            prev_tag = tag
            prev_tok = tok
    return filter(lambda x: x != ('', ''), merged_tags)

def extract_player_relation(toks):
    player = ''
    filler = []
    team   = ''
    for tag, tok in toks:
        if player and team: break
        if tag == 'PERSON':
            player = tok
        elif tag == 'ORGANIZATION':
            team = tok
        else:
            filler.append((tag, tok))
    #print 'Player='+player
    #print 'Team='+team
    fillertxt = ' '.join(map(lambda x: x[1], filler))
    #print 'Filler='+ fillertxt
    regex = re.compile(r'(is|was) (a|an).*(player|plays|member).*(of|for|with).*the')
    match = regex.match(fillertxt)
    player = player.lower().replace(' ', '_')
    team = team.lower().replace(' ', '_')
    if match:
        return ['plays_for', player, team]
    
def initialize_tagger():
    st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
    return st

def tokenize(sentence):
    tokens = word_tokenize(sentence)
    return tokens

def get_tags(tagger, tokens):
    pos = pos_tag(tokens)
    ne_tags = tagger.tag(tokens)
    tags = merge_tags(pos, ne_tags)
    return tags

#print extract_player_relation(tags)

