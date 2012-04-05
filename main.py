#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
import os,sys
from datetime import datetime, timedelta, date

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db

sys.path.append('modules')
from add import AddNoteHandler

class MainHandler(webapp.RequestHandler):
    def get(self):                
                author = 'Jifeng Zhang'
                action = 'programming'
                template_values = {
                }
                #path = os.path.join(os.path.dirname(__file__),'index.html')
                path = os.path.join(os.path.dirname(__file__),'index_simple.html')
                self.response.out.write(template.render(path,template_values))
        
class OolongBasicHandler(webapp.RequestHandler):
    def get(self, id):
        if (id == "overview") or (id == ""):
            template_values = {}
            path = os.path.join(os.path.dirname(__file__),'category.html')
            self.response.out.write(template.render(path,template_values))
        else:
            self.response.out.write(id)

def main():
    add_handler = AddNoteHandler()
    
    application = webapp.WSGIApplication([('/', MainHandler),
                                          (r'/oolong-basic/(.*)', OolongBasicHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
