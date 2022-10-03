# Kartoza Application
Done by Blessed Mutengwa, blessedmutengwa@gmail.com

## Requirements
To be able to run the Application on a local machine, please run the following command without quotes to install the application dependencies and supporting apps:<br>
__"python -m pip install -r requirements.txt"__


## Database
You will need to have installed MySql Database and Xampp application to view database instances using a GUI. <br>Amongst other database applications which include __data warehousing, data store, web applications, mobile, analytics applications__ it is also preferred to handle Geospatial data, which is why it was selected as a database for this application and doesn't require installation of GDAL to work with geo-django or django-gis packages.

## Run Application
To run the application, you will need to locate the root directory for the project and:<br>
1. Migrate the database - type in the terminal the following command without quotes -> python manage.py migrate
2. Run the application server - type in the terminal the following command without quotes -> python manage.py runserver
3. To check if there are any warnings or errors - type in the terminal the following command without quotes -> python manage.py check


## Application Screenshots <br>
### Database [User Table]
<img src="media/screenshots/user_table.png">

### Application [Login Page]
<img src="media/screenshots/login.png">

### Application [Signup Page]
<img src="media/screenshots/register.png">

### Application [Logged Out]
<img src="media/screenshots/logged_out.png">

### Application [Home Page for a user who is also a superuser]
#### _Application Routes has Url for logged-in user current profile and Url for All users since the logged-in user is a super-user_
<img src="media/screenshots/home.png">

### Application [User Profile]
<img src="media/screenshots/about.png">

### Application [User Profile - Where a user can edit their profile]
<img src="media/screenshots/edit_profile.png">

