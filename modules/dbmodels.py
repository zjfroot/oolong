#!/usr/bin/env python
#
# Copyright Jifeng Zhang <zjfroot@gmail.com>.
#
#
from google.appengine.ext import db
class Note(db.Model):
    note = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    user = db.StringProperty()