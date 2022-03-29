# Aletheia - Chrome Extension :heavy_check_mark: :x::pineapple:
Chrome extension that detect fakeness of images.

# Link to chrome web store! - [Aletheia](https://chrome.google.com/webstore/devconsole/2050c6ce-e678-4fbf-853a-c3c2d6a207bc?hl=pt-BR)

## Working
There are two ways of select images to analyze: 

- Local, user select image from computer

- Site, the extension analyze images from current web page.

1. Local Menu, user upload image to extension and then is send to server where is processed by svm model. The response contain image and classification: true or false.
2. Site Menu,images of web site are send to server where is processed by svm model. The response contain image and classification: true or false.

# Components
- Chrome Extension (links)
- Flask Server

# Installation
Before install flask make sure that you have version 3.6 ou newer of python .
- Install [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask)
You can install extension through chrome web store or download all files in respository.
- Download all files and folders from [here](https://github.com/diana-egas/aletheia-chrome-extension)
- Run local server 
`python3 server.py`

# From beginning to end
### Step 1: Analyzing the problem
### Step 2: Creating Chrome Extension
### Step 3: Deploying Flask Server 
### Step 4: Publishing the Extension to Chrome Web Store

![ananas1](https://user-images.githubusercontent.com/38374862/160453804-71b08083-c40b-46d4-97d3-025d9e181536.png)


# References
- Find SVM Model here: [svm](https://github.com/saraferreirascf/Photo-and-video-manipulations-detector/tree/main/Scripts)
