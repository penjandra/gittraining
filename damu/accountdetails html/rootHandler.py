__author__ = 'Om Narayan'
__revision__ = '$'
__version__ = '0.1'
__maintainer__ = 'Om Narayan'
__email__ = 'om.narayan29@gmail.com'
__status__ = 'Prototype'

from baseRequestHandler import BaseRequestHandler
from google.appengine.ext import blobstore
from google.appengine.ext.ndb import *


class RootHandler(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('index.html')

class PriceHandler(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('pricing.html')

class SubscriptionHandler(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('subscription.html')

class AccountDetails(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('account.html')    
 
class FeatureHandler(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('features.html')
  
class AboutusHandler(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('aboutus.html')
   
class ContactusHandler(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('contactus.html')

class ThankYou(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('thankyou.html')
 
class Test(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    upload_url = blobstore.create_upload_url('/file')
    self.response.out.write('<html><body>')
    self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
    self.response.out.write("""Upload File: <input type="file" name="file"><br> <input type="submit"
        name="submit" value="Submit"> </form></body></html>""")
  
class Test1(BaseRequestHandler):
  # @user_required
  def get(self):
    """Handles default langing page"""
    self.render('base_boot.html')
 