#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from dbmodels import *

class AddNoteHandler(webapp.RequestHandler):
    def post(self):
        new_note = self.request.get('note')
    
        note = Note();
        note.note = new_note;
        note.user = "zjfroot@gmail.com";
        note.put();