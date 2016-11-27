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

st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
tokens = word_tokenize(open(sys.argv[1]).read())
pos = pos_tag(tokens)
ne_tags = st.tag(tokens)

tags = merge_tags(pos, ne_tags)

print tags
