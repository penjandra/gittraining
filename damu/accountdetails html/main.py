__author__ = 'Om Narayan'
__revision__ = '$'
__version__ = '0.1'
__maintainer__ = 'Om Narayan'
__email__ = 'om.narayan29@gmail.com'
__status__ = 'Prototype'

import os
import sys
import inspect
# from app.importHandler import *
# from app.authHandler import AuthHandler
from app.demo import Demo
from app.help import Help
from app.about import About
from app.dboard import *
from app.application import *
from app.manageTest import ManageTest
from app.user import *
from app.signupHandler import SignupHandler
from app.logoutHandler import LogoutHandler
from app.loginHandler import LoginHandler

from app.forgotPasswordHandler import ForgotPasswordHandler
from app.verificationHandler import VerificationHandler
from app.setPasswordHandler import SetPasswordHandler


from app.channel import Channel
from app.seleniumLog import *
from app.testcaseLog import *


# user handler

from app.admin import Admin
from app.login import Login

from app.testprofile import *
from app.gridHandler import GridHandler

from app.runResult import RunResult
from app.roboWorkerHandler import RoboWorkerHandler

from webapp2 import WSGIApplication, Route

from google.appengine.ext import deferred 
# Bite 
from app import *


#check production or dev server and based on it load social app config
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
if debug:
    from secrets_dev import *
else:
    from secrets_prod import *
  
# webapp2 config
app_config = {
  'webapp2_extras.sessions': {
    'cookie_name': '_simpleauth_sess',
    'secret_key': SESSION_KEY
  },
  'webapp2_extras.auth': {
    'user_attributes': ['name', ]
  }
}
    
# Map URLs to handlers

routes = [
  Route('/', handler='app.rootHandler.RootHandler', name ="welcome"),
  Route('/home', handler='app.rootHandler.RootHandler', name="home"), 
  Route('/demo', handler= 'app.demo.Demo'), 
  Route('/help', handler='app.rootHandler.RootHandler'),
  Route('/aboutus', handler='app.rootHandler.AboutusHandler'), 
  Route('/features', handler='app.rootHandler.FeatureHandler'), 
  Route('/contactus', handler='app.rootHandler.ContactusHandler'),
  Route('/pricing', handler='app.rootHandler.PriceHandler'), 
  Route('/subscription', handler='app.rootHandler.SubscriptionHandler'),
  Route('/account', handler='app.rootHandler.AccountDetails'),
  Route('/thankyou', handler='app.rootHandler.ThankYou', name='thankyou'), 
  Route('/dashboard', handler='app.dboard.Dboard', name="dashboard"), 
  Route('/dashboardHander', handler='app.dboard.DBoardHandler', name="dashboardHander"), 
  Route('/manageTest', handler='app.manageTest.ManageTest'), 
  Route('/application', handler='app.application.Application'),  
  Route('/appTestHistory', handler='app.application.AppTestHistory'), 
  Route('/appHandler', handler='app.application.AppHandler'), 
  Route('/user', handler='app.user.User', name='user'), 
  Route('/user/checkEmail', handler='app.user.CheckEmail'), 
  Route('/user/signup', handler='app.signupHandler.SignupHandler', name='signup'),
  Route('/user/verification', handler='app.verificationHandler.VerificationHandler', name='verification'),
  Route('/user/setPassword', handler='app.setPasswordHandler.SetPasswordHandler', name='setPasswor'),
  Route('/user/forgot', handler='app.forgotPasswordHandler.ForgotPasswordHandler', name='forgot'),
  Route('/user/login', handler='app.loginHandler.LoginHandler', name='login'),
  Route('/user/signin', handler='app.loginHandler.LoginHandler', name='login'),
  Route('/user/user_profile', handler='app.userHandler.UserHandler', name='login'),

  Route('/user/logout', handler='app.logoutHandler.LogoutHandler', name='logout'),
  Route('/test', handler='app.rootHandler.Test'), 
  Route('/testcase', handler='app.testcase.Testcase'),
  Route('/jobMonitor', handler='app.jobMonitor.JobMonitor'),
  Route('/admin', handler='app.admin.Admin'),
  Route('/channel', handler='app.channel.Channel'),
  Route('/seleniumLog', handler='app.seleniumLog.SeleniumLog'),
  Route('/serveImage', handler='app.seleniumLog.serveImage'),
  Route('/testcaseLog', handler='app.testcaseLog.TestcaseLog'),
  Route('/gridHandler', handler='app.gridHandler.GridHandler'),
  Route('/runResult', handler='app.runResult.RunResult'),
  Route('/roboWorker', handler='app.roboWorkerHandler.RoboWorkerHandler'),
  Route('/team', handler='app.team.Team'),
  Route('/testprofile', handler='app.testprofile.TestProfile'),
  # Route('/testprofileHandler', handler='app.testprofile.TestProfileHandler'),
  Route('/newtestprofile', handler='app.newtestprofile.NewTestProfile'),
  Route(r'/instance/<:\d+>', handler='app.instanceHandler.InstanceHandler'),
  Route(r'/testresult/<:\d+>', handler='app.testcaseResultHandler.TestcaseResultHandler'),

  # bite specific modified by Om
  
  Route('/check_login_status', handler='app.loginHandler.CheckLoginStatus'),
  Route(r'/project/<:\d+>', handler='app.projectHandler.Project'),
  Route('/getproject', handler='app.projectHandler.GetProject'),
  Route('/getprojectnames', handler='app.projectHandler.GetProjectNames'),
  Route('/saveproject', handler='app.projectHandler.SaveProject'),
  Route('/storage/saveproject', handler='app.projectHandler.SaveProject'),
  
  Route('/storage/getprojectnames', handler='app.projectHandler.GetProjectNames'),
  Route('/storage/getproject', handler='app.projectHandler.GetProject'),
  

  Route(r'/project/<:\d+>/bugs', handler='app.projectHandler.GetBug'),

  # Integration
  Route(r'/project/<:\d+>/integration/jira', handler='app.projectHandler.Jira'),

  
  # add bite specific url
  Route('/bugs/urls', handler='app.robo_bite.bugs.handlers.bugs.urls.UrlsHandler'),
  Route('/get_templates', handler='app.robo_bite.handlers.template_handler.GetTemplatesHandler'),
  Route('/new_template', handler='app.robo_bite.handlers.template_handler.NewTemplateHandler'),
  # Route('/bugs', handler='app.robo_bite.bugs.handlers.bugs.create.CreateHandler'),
  Route('/get_my_compat_test', handler='app.robo_bite.handlers.site_compat.MyTestsHandler'),
  # Bug reporting.
  Route('/bugs', handler='app.robo_bite.bugs.handlers.bugs.create.CreateHandler'),
  # bug update 
  Route(r'/bugs/<:\d+>', handler='app.robo_bite.bugs.handlers.bugs.access.AccessHandler'),
  # storage support 
  Route('/storage/add_test_metadata', handler='app.robo_bite.handlers.storage_handler.AddPreexistingDocsMetadata'),
  Route('/storage/gettestasjson', handler='app.robo_bite.handlers.storage_handler.GetTestAsJson'),
  Route('/storage/updatetest', handler='app.robo_bite.handlers.storage_handler.updatetest'),
  Route('/storage/addtest', handler='app.robo_bite.handlers.storage_handler.SaveTest'),
  Route('/storage/savezip', handler='app.robo_bite.handlers.storage_handler.SaveZipFile'),
  Route('/storage/getzip', handler='app.robo_bite.handlers.storage_handler.GetZipFile'),
  Route('/storage/deletetest', handler='app.robo_bite.handlers.storage_handler.DeleteTest'),
  Route('/storage/saveproject', handler='app.robo_bite.handlers.storage_handler.SaveProject'),
  Route('/storage/addscreenshots', handler='app.robo_bite.handlers.storage_handler.AddScreenshots'),
  Route('/storage/getscreenshots', handler='app.robo_bite.handlers.storage_handler.GetScreenshots'),
  
  
]


app = WSGIApplication(routes, config=app_config, debug=debug)
'''
app = WSGIApplication([
                        ('/', RootHandler),
                        ('/profile', ProfileHandler),
                        ('/logout', AuthHandler.logout()),
                        ('/auth/<provider>', AuthHandler._simple_auth),
                        ('/auth/<provider>/callback', AuthHandler._auth_callback),
                      ],
                      config=app_config,
                      debug=True)   
                      
                      '''
