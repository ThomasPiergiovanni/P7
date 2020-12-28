# P7 - Create GrandPy Bot, the old robot!

## 1. Introduction.

This program is named "grandpy". It's a web program that returns places address and Wikipedia information based on a user question. Question such as *Hi Grandpy, do you know what's the address of the Eiffel Tower?* are handled by this program. The program can get the important information of a question like that and provide an answer for it.  
Concretely, the app shows a form where the user can type its question. When submitting the form, the question is sent for parsing. The parsed chain is pushed to Google Place, Map and Wikimedia APIs. The question is then displayed on a chat box along with the program answer, i.e. the address and the Wikimedia info. A map pointing on that place is also displayed.  
Note that this program supports only French language. Question must therefore be in French.  
 
Vist my program : https://thpi-grandpyapp.herokuapp.com

## 2. Prerequisite.
This program requires the following components:
* Python 3.9.0
* Flask 1.1.2
* pytest 6.1.2
* requests 2.25.0
* Google API Keys (*required for using Google services used by this program)*.

## 3. Installation.

### 3.1. Download.
Download/clone this repository on your system, at the location that suits you best.
> git clone https://github.com/ThomasPiergiovanni/P7.git

### 3.2. Python 3 install.
Make sure you have Python 3 installed.
> python --version

If not, you can download it and install it from the [python official website](https://www.python.org/). You will find the necessary documentation there.

### 3.3 Get a Google API Key.
If you  don't have a Google API key, you'll need to get one. Go to Google Cloud Platform the [Google Cloud Platform](https://cloud.google.com/maps-platform/#get-started) for more informations.*

### 3.4. Create & activate a virtual environment (recommended).
In order to avoid system conflicts:

1. Go into your local repository and create a virtual environment using venv package.
> python -m venv env

2. Activate the virtual environment.
> source env/scripts/activate

Documentation is also available on the [python official website](https://www.python.org/).

### 3.5. Flask and Requests install
Install Flask and Requests on you virtual environment using the requirements.txt file.
>pip install -r requirements.txt

Please refer to [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/) for more information.  
Please refer to [Requests certified documentation](https://requests.readthedocs.io/en/master/) for more information.  

### 3.6. Application mandatory settings.
1. Change constants with the appropriate value into **configuration/env.py** :
    * LOCAL = True or False depending if you deploy it locally or not.
    * SECRET_KEY = your environment variable system secret key.
    * GG_API_KEY_BACKEND = An unrestricted Google API key.
    * GG_API_KEY_FRONTEND = An restricted Google API key.

*Note that Google Key restriction is really deployment related. In my case, deploying my app on Heroku servers make that my website IP address is constantly changing. I could therefore not use only one key with Restriction to my app url. I needed to use two, one without restriction, used for backend queries(not visible to user) and one with restriction for front usage. That way I could manage risk of having key stolen by others and have my app running properly*.

For more detailed information on application settings, please check *4.1. env.py* section bellow.

### 3.7. Start the program "GrandPy".
To start the program, type the following in your bash.
> flask run

The program is now ready to be used. Please check *5. Users' guide* section bellow to use it.

*Note that this is the way for starting the app on a local environment. Starting the app on a production environment is different. You'll have to check depending on you deployment environment*

### 3.8. Deactivate the virtual environment.
Once you're done using the program, you should leave the virtual environment. Simply type the following statement in your bash.
> deactivate

### 3.9. Test.
If you want to modify the code, you can run unit test using pytest for testing.  
> pytest

*Note that you shouldn't deactivate the virtual environment if you want to process pytest.*

### 3.10. Uninstall.
If you want to uninstall the program, simply delete the complete repository form your device.

## 4. Settings.
* Changing settings **must be** done in **configuration/env.py** file. Make sure to read *3.6. Application mandatory settings*.
* Changing settings **can be** done in **configuration/config.py** file.

### 4.1. env.py.
Located in **configuration/** package.

#### 4.1.1. LOCAL.
DESCRIPTION: Variable stating whether the program is deployed locally or not.  
MANDATORY: Yes.  
DEFAULT SETTINGS: True.  
CUSTOM SETTINGS: You can replace the default setting depending on the deployment environment.  

#### 4.1.2. SECRET_KEY.
DESCRIPTION: Secret key required for proper Flask usage.  
MANDATORY: Yes.  
DEFAULT SETTINGS: os.environ.get("SECRET_KEY").  
CUSTOM SETTINGS: You need to create environment variable of that name, i.e. SECRET_KEY, with your a secret value(only known to you).

#### 4.1.3. GG_API_KEY_BACKEND.
DESCRIPTION: Google API key required for usage of Google APIs (Backend calls). This key must not restricted.  
MANDATORY: Yes.  
DEFAULT SETTINGS: os.environ.get("GG_API_KEY").  
CUSTOM SETTINGS: You need to create an environment variable of that name in your system i.e. "GG_API_KEY" and with the value of an API key provided by Google. That key must not be restricted on Google API Platform. To get a Google API key or for more info on Google APIs, please check "https://developers.google.com/maps/gmp-get-started".  

#### 4.1.4. GG_API_KEY_FRONTEND.
DESCRIPTION: Google API key for usage of Google Map API (Backend calls). This key must be restricted to its referent (http) if deployed on the web.  
MANDATORY: Yes.   
DEFAULT SETTINGS(1) (if deployment is done locally): os.environ.get("GG_API_KEY").  
DEFAULT SETTINGS(2) (if deployment is done on web): os.environ.get("GG_API_KEY_RESTRICTED").  
CUSTOM SETTINGS: You need to create a environment variables of those name in your system i.e. "GG_API_KEY" and "GG_API_KEY_RESTRICTED" with the value of an API key provided by Google. "GG_API_KEY" don't need to be restricted on Google API Plateform but "GG_API_KEY_RESTRICTED" must. This "GG_API_KEY_RESTRICTED" key is the one used on your production environment. To get a Google API key or for more info on Google APIs, please check "https://developers.google.com/maps/gmp-get-started".

### 4.2. config.py.
Located in **configuration/** package.

#### 4.2.1. COUNTRY
DESCRIPTION: Google Map parameters used to define the default map view.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "France".  
CUSTOM SETTINGS: Can be modified at will. Make sure to update accordingly the LOCATION_BIAS variable as well. For more information, please check "https://developers.google.com/maps/documentation/embed/get-started".  

#### 4.2.2. KEYWORDS
DESCRIPTION: List of words of important usage. Used to analyse which words are important for question parsing.  
MANDATORY: Yes.  
DEFAULT SETTINGS: ["adresse", "trouve"].  
CUSTOM SETTINGS: Modifying this list is not required unless you see that other words should be added to improve parsing analysis.

#### 4.2.3. LOCATION_BIAS
DESCRIPTION: Google Map parameters used to define the bounding box for places finding. Represent the bounding box south-west and north-east corners. In the default case, the bouding box covers all France (metropole).  
MANDATORY: Yes.  
DEFAULT SETTINGS: "rectangle:42.224,-4.727|51.4796,8.3926".  
CUSTOM SETTINGS: Can be modified at will. Make sure it to update accordingly the COUNTRY variable as well.  

#### 4.2.4. STOPWORDS
DESCRIPTION: List of words of common usage. Used to analyse which words are important or not for question parsing.  
MANDATORY: Yes.  
DEFAULT SETTINGS: Default list is available at "https://github.com/6/stopwords-json/blob/master/dist/fr.json".  
CUSTOM SETTINGS: Modifying this list is not required unless you foresee that some other words should be added to improve parsing analysis.  

## 5. Users' guide.

### 5.1. Program functionalities
This program provides the following functionalities:
* User can ask for an address and the program will return, if it understands the question, the address of that place and some more information about that place.

### 5.2. How to.
* Go to the app url e.g. http://localhost:5000/ if deployed locally.  
* Type your question in the text box e.g. "Salut Grandpy, connais tu l'adresse de la Tour Eiffel?" or "Sais-tu ou se trouve l'Arc de Triomphe?". Your question and the program answer will be displayed in the chat box. A map will also dispaly that location if the program found it.
* You can ask questions, till you get bored.
