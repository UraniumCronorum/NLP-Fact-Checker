import sys

import cherrypy

sys.path.insert(-1, '../nlp/')
sys.path.insert(-1, '../logic_component/')

import tagger

import knowledge_base
from rulebases import rb_sports


db = knowledge_base.KnowledgeBase(rb_sports.SportsClaim)

class Server(object):
    def __init__(self):
        self.tgr = tagger.initialize_tagger()
        
    def factcheck(self, txt):
        tokens = tagger.tokenize(txt)
        tags = tagger.get_tags(self.tgr, tokens)
        relation = tagger.extract_player_relation(tags)
        print relation
        ans = db.trueOrFalse(rb_sports.SportsClaim(relation[0], tuple(relation[1:])))
        print ans
        return str(ans)
    
    def index(self):
        return open('index.html').read()

    index.exposed = True
    factcheck.exposed = True

cherrypy.quickstart(Server(), '/', 'app.conf')
