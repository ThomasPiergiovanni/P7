# P7 - Create GrandPy Bot, the old robot!

## !!!! WORK IN PROGRESS!!!!

## 1. Introduction.

This programm is named "grandpy". It's a web programm that returns places address and wikipedia informations based on a user question. Question such as *Hi Grandpy, do you know what's the adress of the Eiffel Tower?* are handled by this programm. The programm can get the important information of question like that and provide an answer for it. 
Concretely, the app present a form where the user can type its question. When submitting the form, the question is sent for parsing. The parsed chain is pushed to Google Place, Map and WikiMedia APIs. The question is then displayed on a chat box along with the programm answer, i.e. the address and the wikimedia infos. A map pointing on that place is also dispalyed.  
Note that this program supports only french language. Question must therefore be in french.  


## 2. Prerequisite.
This program requires the following components:
* Python 3.9.0
* Flask 1.1.2
* pytest 6.1.2
* requests 2.25.0
* Google API Key (*required for using Google services used by this programm)*.


## 3. Installation.

### 3.1. Download.
Download/clone this repository on your system, at the location that suits you best.

### 3.2. Python 3 install.
Make sure you have Python 3 installed.
> python --version

If not, you can download it and install it from the [python official website](https://www.python.org/). You will find the necessary documentation there.

### 3.3 Get a Google API Key.
If you  don't have a Google API key, you'll need to get one. Go to Google Cloud Platerform the [Google Cloud Plateform](https://cloud.google.com/maps-platform/#get-started) for more informations.*


### 3.4. Create & activate a virtual environment (recommended).
In order to avoid system conflicts:

1. Go into your local repository and create a virtual environment using venv package.
> python3 -m venv env

2. Activate the virtual environment.
> source env/Scripts/activate

Documentation is also available on the [python official website](https://www.python.org/).

### 3.5. Flask and Requests install
Install Flask and Requests on you virtual environement using the requirements.txt file.
>pip install -r requirements.txt

Please refer to [Flask documention](https://flask.palletsprojects.com/en/1.1.x/) for more informations.
Please refer to [Requests certified documentation](https://requests.readthedocs.io/en/master/) for more informations.

### 3.6. Application mandatory settings.
1. Rename **configuration/env.py.example** file into **configuration/env.py**.
2. Change constants with the appropriate value into **env.py**:
    * SECRET_KEY = your environnement variable system secret key.
    * GG_API_KEY = your Google API key.

For more detailed informations on application settings, please check *4.1. env.py* section bellow.

### 3.7. Start the programm "GrandPy".
To start the programm, type the following in your bash.
> flask run

The programm is now ready to be used. Please check *5. Users' guide* section bellow to use it.

### 3.8. Deactivate the virtual environment.
Once you're done using the program, you should leave the virtual environment. Simply type the following statement in your bash.
> deactivate

### 3.10. Test.
If you want to modify the code, you can run unit test using pytest for testing.
> pytest grandpy/

### 3.9. Uninstall.
If you want to uninstall the program, simply delete the complete repository form your device.

## 4. Settings.

* Changing settings **must be** done in **env.py** file. Make sure to read *3.6. Application mandatory settings*.
* Changing settings **can be** done in **config.py** file.

### 4.1. env.py.
Located in **configuration/** package.

#### 4.1.1. SECRET_KEY.
DESCRIPTION: Secret key required for proper Flask usage.  
MANDATORY: Yes.  
DEFAULT SETTINGS: os.environ.get("SECRET_KEY") or "you-will-never-guess".  
CUSTOM SETTINGS: You must repalce the default "you-will-never-guess" with a string of yours own knowledge.  

#### 4.1.2. GG_API_KEY.
DESCRIPTION: Google API key required for usage of google APIs.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "your-google-api-key".  
CUSTOM SETTINGS: You must replace the default key with your own google api key. Fore more informations, please check "https://developersgoogle.com/maps/gmp-get-started".  


### 4.2. config.py.
Located in **configuration/** package.

#### 4.2.1. CONNECTION_ERROR
DESCRIPTION: Message dispalyed when connection to client API is failing.  
MANDATORY: Yes.  
DEFAULT SETTINGS: (  
               "Un problème de connection est apparu. Ré-essaayez plus"  
               " tard ou contacter le propriétaire de l'application")  
CUSTOM SETTINGS: Can be modified but there is no real sense to do so.  

#### 4.2.2. COUNTRY
DESCRIPTION: Google Map parameters used to define the default map view.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "France".  
CUSTOM SETTINGS: Can be modified at will. Make sure to update accordingly the LOCATION_BIAS variable as well. For more information, please check "https://developers.google.com/maps/documentation/embed/get-started".  

#### 4.2.3. KEYWORDS
DESCRIPTION: List of words of important usage. Used to analyze which words are imortant for question parsing.  
MANDATORY: Yes.  
DEFAULT SETTINGS: ["adresse", "trouve"].  
CUSTOM SETTINGS: Modifying this list is not required unless you see that other words should be added to improve parsing analysis.

#### 4.2.4. LOCATION_BIAS
DESCRIPTION: Google Map parameters used to define the bounding box for places finding. Represent the bouding box south west and north east corners. In the default case, the bouding box covers all France (metropole).  
MANDATORY: Yes.  
DEFAULT SETTINGS: "rectangle:42.224,-4.727|51.4796,8.3926".  
CUSTOM SETTINGS: Can be modified at will. Make sure it to update accordingly the COUNTRY variable as well.  

#### 4.2.4. STOPWORDS
DESCRIPTION: List of words of common usage. Used to analyze which words are imortant or not for question parsing.  
MANDATORY: Yes.  
DEFAULT SETTINGS: Default list is available at "https://github.com/6/stopwords-json/blob/master/dist/fr.json".  
CUSTOM SETTINGS: Modifying this list is not required unless you forseas that some other words should be added to improve parsing analysis.  

## 5. Users' guide.

### 5.1. Program functionalities
This program provide the following functionalities:
* NA

### 5.2. How to.
* NA
