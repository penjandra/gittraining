RobusTest
=========

### Installation
### Prerequisite 
* python2.7+
* Java 1.6+
        
### How Install Google App Engine :
* Download Google_App_Engine_SDK_for_Python(http://googleappengine.googlecode.com/files/google_appengine_1.8.3.zip)
* Extract and save to /appengine

###  Usages

### How to Start RobuTest web server for development
* go to source_home_folder (command line)
* run "python /appengine/dev_appserver.py googleApp/"
* it will start web server on port 8080

### How to edit html :
* to see the changes, open respective page (localhost:8080/page) 
* for more information please refer - http://jinja.pocoo.org/docs/

### How to edit javascripts:
* javascript loacation : /source_home_folder/googleApp/static/js
* how to call in template : use relative url that is "/js/javascrit_file"
* Please prefer inline javascript - () 

### How to edit css:
* javascript loacation : /source_home_folder/googleApp/static/css
* how to call in template : use relative url that is "/css/css_file"
* Please prefer inline css - () 

### Images :
* image loacation : /source_home_folder/googleApp/static/img
* how to call in template : use relative url that is "/img/image_file"

## Testing  :

#### run google app engine 
python /googleAppEngine/dev_server.py /path_to_robustest/googleappengine

### run roboworker 
python /googleAppEngine/dev_server.py /path_to_robustest/roboworker/robustestworker.py 

### run selenium 
* java -jar selenium-standalone.jar -role hub -hubConfig hub.config
* java -jar selenium-standalone.jar -role node -nodeConfig node.config  -Dwebdriver.chrome.driver=/opt/chromedriver

### Register roboworker 
make post request to - http://localhost:8080/roboWorker


### Resister selenium 
make post request to - http://localhost:8080/gridHandler



