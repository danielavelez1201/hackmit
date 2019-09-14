import webapp2
import jinja2
import os
import logging
import datetime
now = datetime.datetime.now()

from google.appengine.api import images

from google.appengine.api import users
from google.appengine.ext import ndb

class Profile(ndb.Model):
    name = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)

class Case(ndb.Model):
    profile = ndb.KeyProperty(kind = Profile)
    name = ndb.StringProperty(required = True)
    client = ndb.StringProperty(required = True)
    type = ndb.StringProperty(required = True)
    description = ndb.StringProperty(required = True)
    date = ndb.StringProperty(required = True)


class addCase(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/addCase.html')
        self.response.write(template.render())
    def post(self):
        user = users.get_current_user().email()
        profile = Profile.query().filter(user == Profile.email).get()
        profileKey = profile.key
        name = self.request.get("name")
        client = self.request.get("client")
        type = self.request.get("type")
        description = self.request.get("description")
        date = now.date
        location = self.request.get("location")
        case = Case(profile = profileKey, name = name, client = client, type = type, description = description, date = date, location = location)
        case.put()
        self.redirect('/index')
