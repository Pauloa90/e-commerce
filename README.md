[![Build Status](https://travis-ci.org/Pauloa90/e-commerce.svg?branch=master)](https://travis-ci.org/Pauloa90/e-commerce)

# E-Go
Full Stack Framework with Django Milestone Project


This is an Ecommerce website built with Python, Django as a python’s framework from Code Institute.
E-go is a fictitious e-commerce website that provides holidays packages for users who want to buy this service to go on holidays. 
The website will provide the price and more details for different places to go, cultural aspects and curiosities about different coutries as well.

![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/homepage01.PNG)

This project has incorporated code pulled from other projects given by Code Institute:

1. django-e-commerce project
2. django-auth

The course of Code Institute guided me durnig this project.

## Summary 
1. Live Demo
2. UX
    - User Stories
    - Strategy
    - Scope
    - Strutucte

3. Wireframes
 - Home
 - Discover
 - Curiosities
4. Installation
5. Technology used
6. Features 
7. Features do be Implemented
8. Deployment
9. Testing
10. Credits

## Live Demo
Please check the link to see the deployed version of the app: [link](https://ecommercego.herokuapp.com/)

Please check the link for Screeshots:
1. [Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/screeshot01.PNG)
2. [Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/screeshot02.PNG)
3. [Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/screeshot03.PNG)
4. [Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/screeshot04.PNG)
5. [Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/screeshot05.PNG)
6. [Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/screeshot06.PNG)
7. [Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/screeshot07.PNG)
 



## UX
### User Stories


This site is for any user interested in going on holidays, looking for a single site where you can find a package with hotels, experiences, curiosities about different countries in just one web page.

E-commerce is only online at the moment, depending on customers' wishes, a special web application can be designed to have in a store.
A super user was created to add the products (packages) and the user can also register to send the payment.

As a new user of the webpage, I'd like to be able to:
- Find out what I can get to know on this website.
On the landing page the user can already see the e-commerce with all the products (packages) he is able to buy.

![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/user01.PNG)

- Get to know more about travelling from different people. 
The user is able to check the session "Discover" and hear from different people their stories. On this session the user get the links of many blogs regarding travelling.
![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/user02.PNG)

- If the user still doesnt know about where to go, they can check curiosities about places that the website is selling the packge to, such as Brazil, New Zealand and Thailand.
On the session "curiosities" the user will get to know some fun and interesting things about some places thar the website is selling the package to.
![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/user03.PNG)

- The user is able to register themself in order to purchase some thing from the webpage.
The user will have to fill a form in order to do it.
![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/user04.PNG)

- The user is able to choose packages of holidays and get to see it before finishing the order.
When the products are in the cart, the user can amend the order, deleting or adding a new product.
![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/user05.PNG)

### Strategy 
E-go is a simple web ecommerce to make peoples lives eaiser regarding travelling. On the webpage they can get to know more about travelling through the blogs and also curiosities from diffenrent places.
The owner can negotiate with travel agencies and have more products on the webpage which can be really profitable for both.

### Scope
I wanted from the begging have a webpage easy to access from the user's side, and fun to get to know different blogs. On the navbar there are only 3 options being "Home" where the ecommerce is hoted,
"Curiosities" thar provides interesting stories and facts about places being sold on the ecommerce and "Discover" where users can access many Blogs that post things about trips, travelling and etc.

### Structure
The user arriving on the main page, they can get to see a navbar on top with the session that they have access on the left side, and on the right side a Login area.
Once that the user is regirested on website, they are able to purchase any product. To register the user has to give a Login username, password and email. If the user forgets the password, they can access "Reset Password" and they will receive
an email to have a new password. In both cases a feedback message will appear.

The User can simply add the quantity of the package in the cart by clicking  on blank field of the cart with the product that they wish, and add a number (people) on it and then click on "add".
The User is redirect to main page again giving the opportunitty to add another product (package). If that is not the case the user can go o "cart" on the right top side of the navbar and be redirect to the checkout session.

Once the order is according to what the user chose, clicking on "checkout" and add the payment details required, the order will be processed by stripe. If there is anything to amend, the user can change the quantity in the respective field and click on "amend".
If the user wants to delete the item, they can simply type "0" on the field and "amend" right after and the product will be deleted.

In both scenarios, payment processed successufully or not, a feedback message will appear to the user. If the payment is processed the user is redirected to the main page again.

In Discover section, the user can click on the Blogs which is more interesting for thenself and another tab will open on the browser making sure the user does not lose track and gets away from the webpage.

In the Section "Curiosities", Jumbotrons with images and text with fun facts about different countries will be shown.

### Wireframes
Here are the 3 wireframes for each section of my project:
#### Home
![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/wireframes01.jpeg)
#### Discover
![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/wireframes02.jpeg)
#### Curiosities
![Screeshot](https://ecommercego.s3-eu-west-1.amazonaws.com/media/wireframes03.jpeg)

## Installation
To be able to create the app the folowing steps were taken:

1. Start with gitpod full template and install Django with the following comand: pip3 install django==1.11.24

2. CReate a project with django: django-admin startproject ecommerce

3. Download this project by cliking the [link](https://github.com/Pauloa90/e-commerce)

4. Create env.py and .gitignore to keep your secret keys safe.

5. Set up a Strip account and keep the secret key safe on .gitignore

6. Create an Amazon account and crate a bucket to store your media on S3 services provided by amazon.

7. Type on the terminal "python manage.py migrate" to apply migrations to your local sqlite database.

8. "python3 manage.py createsuperuser" will create a user able to add files to the database or create a new database.

9. To run the project type on terminal "python3 manage.py runserver".



## Technology used

1. HTML5
2. CSS3
3. Python
4. JAVASCRIPT
5. Django
6. Bootstrap
7. JQuery
8. GitHub/GitPod

## Features

Navigation bar is visible on all pages and also the search field in a Jumbotron. If the screen becomes smaller it toggles and the user is able to visualise it on click.
Footer is also visible in every page with social media links.
E-commerce as the main page the user can purchase a product.


## Features do be Implemented
There were a few Features left to be Implemented:
- Contact form - will make the user able to contact the owner of the ecommerce.
- Newsletter - the users will receive any update from the webpage with deals and good offers.
- Social media - the webpage is ready to change the link if the ownerhas other social medias such as Facebook, Instagran, etc.

## Deployment
In order to deploy this project a python package Gunicorn was installed and Heroku is the hoster of this project.
For Storaging the package Pillow has been installed. AWS (Amazon Web Services) S3 was used to store media files and Boto3 to connect to project to it.
The project has been styled using Font Awesome, Bootstrap and Django-Forms Bootstrap to allo the usage of Bootstrap in templates.

I used Heroku services to deploy my project using Postgres database though the following steps:

- On gitpod install: "pip3 install dj-database-url". This will allow connection to a database
- Install psycopg2 typing "pip3 intall psycopg2" which will allow connection to the postgres database.
- Create requirements.txt typing "pip3 freeze>requirements.txt"
- Change deafult sqlite database to : DATABASES = { 'default' :dj_database_url.parse(os.environ.get('DATABASE_URL')) }
- Add DATABASE_URL config vars code to env.py 
- Make migrations to migrate all database typing "python3 manage.py makemigrations" and "python3 manage.py migrate"
- Install gunicorn typing "pip3 isntall gunicorn"
- Create Procfile 
- Add heroku to ALLOWED_HOST = []

### Testing
Travis has been used for testing the project.
HTML and CSS validators were used to ensure identation and error wont accur.


## Credits


#### New Zealnd <br/> 
[link](https://www.newzealand.com/in/nature-and-wildlife/)<br/>


#### Cancun <br/>
[link](https://www.mexicancaribbean.travel/cancun/)<br/>

#### Madagascar <br/>
[link](https://www.booking.com/hotel/mg/heure-bleue.html)<br/>

#### Angra Dos Reis <br/>
[link](https://media-cdn.tripadvisor.com/media/photo-s/0f/73/be/04/img-20170423-125021-360.jpg)<br/>

#### Coles Bay <br/>
[link](https://en.wikipedia.org/wiki/Coles_Bay,_Tasmania)<br/>
[link](https://cdn.broadsheet.com.au/cache/ba/f0/baf05ddfb005ae00d701ec6a69abb59e.jpg)<br/>
[link](https://www.cntraveler.com/galleries/2015-12-18/the-10-best-beaches-in-australia)<br/>

#### Turkey Beaches <br/>
[link](https://travelaway.me/best-beaches-turkey/)<br/>



