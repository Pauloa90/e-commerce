# E-Go
Full Stack Framework with Django Milestone Project



This is an Ecommerce website built with Python, Django as a python’s framework from Code Institute.
E-go is a fictitious e-commerce website that provides holidays packages for users who want to buy this service to go on holidays. 
The website will provide the price and more details for different places to go to such as main sightseeings, most import places and bit of the cultural aspects.

This project is incorporates code pulled from other projects give by Code Institute:

1. django-e-commerce project
2. django-auth

## Live Demo
Please check the link to see the deployed version of the app: [link](https://ecommercego.herokuapp.com/)

Please check the link for a WireFrame and Screeshot:
1. [Screeshot]()
2. [Screeshot]()
3. [Screeshot]()
2. [WireFrame]()


## User Experience

This website is for any user interested in going on holidays, looking for one single website where they can find a package with hotel, flight and experiences in just one place.
The ecommerce is only online at the moment, depending on the clients wish, a special web app can be designed to have in a store.
A super user was created in order to add the products (packages) and user can also register in order to submit the payment.

The course of Code Institute was my guide during the project.

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

## Heroku 
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

E-commerce - user is able to add a product into the cart, check out and pay for the product.#
Products - Super user can add, edit and delete a product to display on the app.
Navigation - User is able to see the products, and search for a product.

## Features do be Implemented
There were a few Features ledt to be Implemented:
- Contact form 
- Hotels
- Cultures

## Deployment
In order to deploy this project a python package Gunicorn was installed and Heroku is the hoster of this project.
For Storaging the package Pillow has been installed. AWS (Amazon Web Services) S3 was used to store media files and Boto3 to connect to project to it.
The project has been styled using Font Awesome, Bootstrap and Django-Forms Bootstrap to allo the usage of Bootstrap in templates.

### Testing
Travis has been used for testing the project.
HTML and CSS validators were used to ensure identation and error wont accur.


## Credits


### Cards Content - Set your goal
#### New Zealnd <br/> 
[link](https://www.newzealand.com/in/nature-and-wildlife/)<br/>


#### Cancun <br/>
[link](https://www.mexicancaribbean.travel/cancun/)<br/>

#### Madagascar <br/>
[link](https://www.booking.com/hotel/mg/heure-bleue.html)<br/>

#### Angra Dos Reis <br/>
[link]https://media-cdn.tripadvisor.com/media/photo-s/0f/73/be/04/img-20170423-125021-360.jpg)<br/>

#### Coles Bay <br/>
[link]https://en.wikipedia.org/wiki/Coles_Bay,_Tasmania)<br/>
[link]https://cdn.broadsheet.com.au/cache/ba/f0/baf05ddfb005ae00d701ec6a69abb59e.jpg)<br/>
[link](https://www.cntraveler.com/galleries/2015-12-18/the-10-best-beaches-in-australia)<br/>

#### Turkey Beaches <br/>
[link](https://travelaway.me/best-beaches-turkey/)<br/>



