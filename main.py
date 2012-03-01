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
        user = users.get_current_user()
        if user:
            if user.email() == "zjfroot@gmail.com":
                #get word list
                query = db.GqlQuery("SELECT * FROM Note ORDER BY created DESC LIMIT 30")
                notes = query.fetch(20)
                notes_today = []
                notes_yesterday = []
                notes_older = []
                for note in notes:
                    diff = (date.today() - note.created.date())
                    if diff == timedelta (days = 0):
                        notes_today.append(note)
                    elif diff == timedelta (days = 1):
                        notes_yesterday.append(note)
                    else:
                        notes_older.append(note)
                
                author = 'Jifeng Zhang'
                action = 'programming'
                template_values = {
                    'author':author,
                    'action':action,
                    'notes_today':notes_today,
                    'notes_yesterday':notes_yesterday,
                    'notes_older':notes_older,
                }
                path = os.path.join(os.path.dirname(__file__),'index.html')
                self.response.out.write(template.render(path,template_values))
            else:
                self.redirect(users.create_login_url(self.request.uri))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    
        


def main():
    add_handler = AddNoteHandler()
    
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/add', AddNoteHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
