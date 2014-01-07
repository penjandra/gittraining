__author__ = 'Om Narayan'
__revision__ = '$'
__version__ = '0.1'
__maintainer__ = 'Om Narayan'
__email__ = 'om.narayan29@gmail.com'
__status__ = 'Prototype'


import cgi
import json

from baseRequestHandler import *

from google.appengine.api import users
from datastore.project import Project

from webapp2_extras.auth import InvalidAuthIdError
from webapp2_extras.auth import InvalidPasswordError

userFields = ['email', 'password']
class UserHandler(BaseRequestHandler):

  def _on_signin(self, emailId):
    user = self.auth.store.user_model.get_by_auth_id(emailId)
    if user:
      logging.info('Found existing user "%s" to log in' % emailId)
      if self.logged_in:
        logging.info('User "%s" is already logged in.' % emailId)
      else :
        logging.info('User "%s" is not loggded in.' % emailId)
        self.auth.set_session(
            self.auth.store.user_to_dict(user))
      return True
    else :
      logging.info('New user "%s" found.' % emailId)

  def get(self):
    print 'inside User Handler : get method'
    if self.logged_in:
      if self.current_user.verified:
        self.render('user_profile.html')
        #This one should work but.. not going here.. TODO
      else:
        self.render('user_profile.html')
    else:
      self.render('signin.html')
      # self.redirect(self.uri_for('thankyou'))   --- this is not required for signin...



  def post(self):
    print 'inside loging handler: post method'
    userData = dict(cgi.parse_qsl(self.request.body))
    self.response.set_status(400)
    message = None
    if userData:
      for key in userFields:
        if key not in userData or not userData[key]:
          message = "'%s' is missing." % key
    else:
      message = "Please enter email and password."
    print 'message', message, userData
    if not message:
      try:

        if self.logged_in:
          logging.info('User "%s" is already logged in.' % userData['email'])
          # logout from the current session
          self.auth.unset_session()
        user = self.auth.store.user_model.get_by_auth_password(userData['email'], userData['password'])
        print 'inside loging handler: post method 2nd time' 

        if user:
          self.response.set_status(200)
          self.auth.set_session(
              self.auth.store.user_to_dict(user))
          message = "Loging successful"
        else:
          message = "Invalid ID or password. Please try again"


        #self.redirect(self.uri_for('dashboard'))
      except (InvalidAuthIdError, InvalidPasswordError) as e:
        logging.info('Login failed for user %s because of %s', userData['email'], type(e))
        message = "Invalid ID or password. Please try again"

    jsonData = json.dumps({"msg" :message})
    self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
    self.renderJson({"msg" :message})
    #self.render('', {"message" : "%s doesnt exist."})


