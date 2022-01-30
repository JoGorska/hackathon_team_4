# Contents
- [Contents](#contents)
- [NameUnspecified](#nameunspecified)
  * [UX](#ux)
    + [Purpose](#purpose)
    + [User Stories](#user-stories)
    + [Wireframes](#wireframes)
    + [Agile Methodology](#agile-methodology)
  * [Existing Features](#existing-features)
    + [Navbar and Footer](#navbar-and-footer)
    + [Home page](#home-page)
    + [Feature ddd](#feature-ddd)
  * [Future Features](#future-features)
    + [feature 1](#feature-1)
    + [Feature 2](#feature-2)
  * [Technologies Used](#technologies-used)
    + [Languages Used](#languages-used)
    + [Technologies and Programs Used:](#technologies-and-programs-used-)
    + [Frameworks Libraries and Programs Used](#frameworks-libraries-and-programs-used)
  * [Code Validation](#code-validation)
    + [HTML beautify](#html-beautify)
    + [HTML valiation](#html-valiation)
    + [CSS validation](#css-validation)
    + [JavaScript validation](#javascript-validation)
    + [Python beautify](#python-beautify)
    + [Python validator](#python-validator)
  * [Tests](#tests)
    + [Automated tests](#automated-tests)
    + [Lighthouse](#lighthouse)
    + [Manual tests](#manual-tests)
      - [First release](#first-release)
  * [Project Bugs and Solutions:](#project-bugs-and-solutions-)
    + [bug...](#bug)
  * [Deployment and making a clone](#deployment-and-making-a-clone)
    + [Deployment to heroku](#deployment-to-heroku)
    + [Forking the GitHub Repository](#forking-the-github-repository)
    + [Making a Local Clone](#making-a-local-clone)
    + [Setting up your local enviroment](#setting-up-your-local-enviroment)
  * [Credits](#credits)
    + [Online resources](#online-resources)
    + [Tutorials and inspiration](#tutorials-and-inspiration)
    + [People](#people)




# NameUnspecified

[![showpiece home page](link/to/img)](https://self-care-app-hackathon.herokuapp.com/)

Click [here](https://self-care-app-hackathon.herokuapp.com/) to live site.  

## UX
------

### Purpose

The success of any organisation depends on the wellness and wellbeing of the workforce. A positive and proactive approach by employers to monitor and promote positive mental health impacts not only productivity, but also employee health and company culture.

Stress and poor mental health prevent employees being fully focused on their work, and can eventually lead to burn-out and absenteeism, impacting company costs and output. COVID-19 has rapidly increased the importance of employers implementing tools and processes to protect the mental health and wellbeing of their workforce.

The MyMindsEye website provides both employers and their teams with a simple and effective way of monitoring mental health, as well as offering simple and practical tools to take action when needed.

### User Stories

The following user stories were satisfied: 

**As a user you can:** 

#1 Register to the website by using your email address and choosing a password to gain access.  

#2 Log-in everyday with your user-name and password and record how you are feeling. 

#3 Navigate to the relevant page to get tips on how you are feeling. 

#3 Get tips on the mood you are feeling today or other moods you might be feeling. 

#4 Get information on sleep and tips for better sleeping.  

#5 Get information on a sleep technique to help you sleep. 

#6 Navigate back to the home page to choose another emotion. 

#7 Get information if you are bored and tips on what to do if you are bored. 

#8 Play a game if you are bored. 

#9 Get information on happiness and tips on keeping yourself happy. 

#10 Get information on stress and tips on how to manage that stress for work, exams or everyday life. 

#11 Take a breather and breathe with the timing of the lungs to help manage stress. 

#12 Check your mood history. 

#13 Navigate back to the homepage easily. 

#14 Log-out easily. 


### Wireframes 

The website is designed to mobile first and responsive.  

Wireframes were created with [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiAubmPBhCyARIsAJWNpiMYzrk_0rLzl3vgYKRLXwnX7rpqyQiUFdyt3xHGpRiHlZlozwO_pvcaAvUFEALw_wcB).  Initital wireframes were made and then modified. 

Wireframes design was focused on emotions and letting the user select how they were feeling the day they logged in.  

Wireframes final version can be found [here](/workspace/hackathon_team_4/static/media/readme/wireframes-mymind.pdf)

 


### Agile Methodology

![Screenshot of the canban board](im/here)(link-to/canba)

Github issues were used to create the User stories and group them according to MoSCoW prioritization technique. Link to the project with live issues can be found [here](https://github.com/JoGorska/mileage-tracker/projects/1). The issues are currently in two categories - done or for the next relese. 

The issues were than closed automaticaly when the pull request was linked to the issue. 

## Existing Features
------

### Navbar and Footer

xx

### Home page 

dd

### Feature ddd





## Future Features 
------

### feature 1



d

### Feature 2
dd




## Technologies Used
------

### Languages Used

   + HTML5
   + CSS3
   + JavaScript
   + jQuery
   + Python
   + Django

### Technologies and Programs Used:
+ GitHub
    The Git was used for version control
    Git issues were used for user stories
    GitPod was used as IDE to write the code and push to GitHub
+ Heroku 
    The page was deployed to Heroku
+ PostgreSQL
    PostgreSQL was used as database for this project
+ VSCode
    VSCode was used on the days when GitPod was down
+ Google Cloud
    to get api key
+ cloudinary storage
    for storing static files

 ### Frameworks Libraries and Programs Used

+ Balsamiq:
    Balsamiq was used to create the wireframes during the design process.
+ Bootstrap 5:
    Bootstrap was used to add style to the website.
+ Bootswach:
    Bootswatch wass added to change the standard styling and color pallette provided by bootstrap
+ Bootstrap icons
+ Django

## Code Validation
------

### HTML beautify

 [online HTML code Beautifier](https://htmlbeautify.com/). 

### HTML valiation

[HTML validator](https://validator.w3.org/nu/#textarea)


| Page  |  result
| ------ | ------ |
|  [Home](link/to/report |  No errors |
|  [another page](link/to/file.pdf)|No errors|



### CSS validation

[W3C validator](https://jigsaw.w3.org/css-validator/). The copy of the CSS report can be found [here](.....)

### JavaScript validation
Javascript code validation was complited on [jshint](https://jshint.com/)
Initialy it was returning errors in relation of ES6 syntax, which was resolved by adding this line to the beggining of the file
```
/*jshint esversion: 6*/
```

| Page  |  result
| ------ | ------ |
|  [script](link to result here /???) |  no errors |



### Python beautify
All pages were initialy put through [Python Formatter](https://codebeautify.org/python-formatter-beautifier) which automaticaly sorted most of the too long lines errors. Than the code was checked by pylint and problems were displayed in the console. Once the issues were cleared I have put all code though pep8 validator.

### Python validator

Pylint was used to verify Python code. Any errors were corrected and re-run until correct. In some cases, where linting errors were erroneous or unavoidable these were suppressed. Files generated by django and unit tests were ignored.

*R0903* (too-few-public-methods) error ignored for .forms Classes as all forms are designed to store information, populate the database, and iterate through form data in templates.

*R0901* (too-many-ancestors) error ignored for .views as Classes inherit too many ancestors from Django base classes.

*E1101* (no-member) errors are ignored for all apps, as Django dynamically adds 'objects' Manager instance to all models, but pylint is unable to detect this.

*W0612* (unused-variable) errors ignored for wellbeing.views as variables would be used for future functionality

*W0611* (unused-import) error ignored for user_account.urls and settings.py as these are erroneous.

## Tests
------

### Automated tests

Automated tests have not been created due to time constrains of the project.

### Lighthouse


### Manual tests

#### First release

**Release main fetures:**

llll



## Project Bugs and Solutions:
------
### bug...
dddd





## Deployment and making a clone

### Deployment to heroku

**In your app** 

1. add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
2. Git add and git commit the changes made

**Log into heroku**

3. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in

4. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

5. Write app name - it has to be unique, it cannot be the same as this app
6. Choose Region - I am in Europe
7. Click "Create App"

**The page of your project opens.**

8. Go to Resources Tab, Add-ons, search and add Heroku Postgres

9. Choose "settings" from the menu on the top of the page

10. Go to section "Config Vars" and click button "Reveal Config Vars". 

11. Add the below variables to the list

    * Database URL will be added automaticaly
    * Secret_key - is the djnago secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
    * Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register. 
    * Google API key can be obtained [here](https://cloud.google.com/gcp?authuser=1) you will have to register with google and create new app to get the API key. Follow the instructions on the website.

**Go back to your code**

12. Procfile needs to be created in your app
```
web: gunicorn PROJ_NAME.wsgi
```

13. In settings in your app add Heroku to ALLOWED_HOSTS

14. Add and commit the changes in your code and push to github

**Final step - deployment**

15. Next go to "Deploy" in the menu bar on the top 

16. Go to section "deployment method", choose "GitHub"

17. New section will appear "Connect to GitHub" - Search for the repository to connect to

18. type the name of your repository and click "search"

19. once Heroku finds your repository - click "connect"

20. Scroll down to the section "Automatic Deploys"

21. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

22. Click "Deploy branch"

Once the program runs:
you should see the message "the app was sussesfully deployed"

23. Click the button "View"

The live link can be found [here](live/page/here/???).

### Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](repo here???)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](repo here???)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open commandline interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone http..repo here???
```

7. Press Enter. Your local clone will be created.

### Setting up your local enviroment

1. Create Virtual enviroment on your computer or use gitpod built in virtual enviroment feature.

2. Create env.py file. It needs to contain those 5 variables.

* Database URL can be obtained from [heroku](https://dashboard.heroku.com/), add PostgreSQL as an add on when creating an app. 
* Secret_key - is the djnago secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
* Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register. 
* Google API key can be obtained [here](https://cloud.google.com/gcp?authuser=1) you will have to register with google and create new app to get the API key. Follow the instructions on the website.

```
os.environ["DATABASE_URL"] = "..."
os.environ["SECRET_KEY"] = "..."
os.environ["CLOUDINARY_URL"] = "..."
os.environ["GOOGLE_API_KEY"] = "..."
os.environ["DEVELOPMENT"] = "True"
```

3. Run command 
```
pip3 install -r requirements.txt
```

## Credits 
### Online resources
* [Google Fonts]()
* [Icons8](https://icons8.com/)
* [Flaticon](https://www.flaticon.com/)
* [unsplash](https://unsplash.com/)
* [Fontawsome](https://fontawesome.com/)
* [Bootstrap 5]()
* [Markdown best practices](https://www.markdownguide.org/basic-syntax/)
* [Markdown Table of content generator](http://ecotrust-canada.github.io/markdown-toc/)
* [How to do typewriter font](https://www.w3schools.com/howto/howto_js_typewriter.asp)

### Tutorials and inspiration

* The project walkthrough I Think Therefore I Blog tutorial provided instpiration for traffic alerts the repository can be found [here](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/12_final_deployment/blog/views.py)

* The Sleep Technique was found on the website [healthline.ie](https://www.healthline.com/health/4-7-8-breathing#How-to-do-it-)

* Inspiration for the introduction to the importance of sleep was provided from an article written by Alison Brown, MSc. and can be found [here](https://jameskirkbernardfoundation.org/featured/sleep-matters/?gclid=Cj0KCQiA6NOPBhCPARIsAHAy2zC1wcK7zm3QaHnZleHyxBdekrOKmQhFIwGv_Fos3FxaNdwv2PbIAG0aAkIUEALw_wcB) 

* Total Health Pharmacy provided a lot of information and inspiration for the tips and content.  In particular their info-graphics.  Click [here](https://www.totalhealth.ie/) for more information on Total Health Pharmacy. 

* The inspiration for the boredom content can be found [here](https://www.dummies.com/article/body-mind-spirit/emotional-health-psychology/emotional-health/mindfulness/how-to-overcome-boredom-and-restlessness-to-practice-mindfulness-164027) and [here](https://www.medicalnewstoday.com/articles/325697)







### People


