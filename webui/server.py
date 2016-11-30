import sys

import cherrypy

sys.path.insert(-1, '../nlp/')

import tagger

class Server(object):
    def __init__(self):
        self.tgr = tagger.initialize_tagger()
        
    def factcheck(self, txt):
        tokens = tagger.tokenize(txt)
        tags = tagger.get_tags(self.tgr, tokens)
        relation = tagger.extract_player_relation(tags)
        return relation
    
    def index(self):
        return open('index.html').read()

    index.exposed = True
    factcheck.exposed = True

cherrypy.quickstart(Server(), '/', 'app.conf')
