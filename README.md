# NEWS API

## This API is deployed [here](https://hitori-newsapp.herokuapp.com/api/articles/)

### Local Deployement

##### First of all create a virtual environment for python. Depending on the OS [follow these instructions](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### Through command line enter the root of the project folder.
-----
```
cd news_api
```

##### Activate the environment you created by the following commands on the terminal
-----

```
source env/bin/activate
```

##### Install all the requirements provided by following command
-----
```
pip install -r requirements.txt
```

##### Now you have installed all the dependencies. For simplicity purposes, we are using SQLite3

##### Finally, it's time to map the database design and start the project
----
```
python manage.py migrate
python manage.py createsuperuser
# enter a username, password, and confirm password. This will be your first superuser which will help you enter the admin panel of Django
python manage.py runserver
```

##### Now go to the localhost and enter the username and password you created in the last step. You are in the admin panel now and the backend is set up for use.
&nbsp;
### Heroku Deployment

##### Go to [Heroku](https://www.heroku.com/) and signup to create a new account.
##### Now create a new app inside your account, give it a acceptable name, for example -> news_api
##### Now go to the folder provided to you through the delivery and enter the root folder
---
```
cd news_api
```

##### Alternatively you can clone the repository provided to you in the delivery and clone the repo
----
```
git clone https://github.com/Par010/news_api.git
cd news_api
```

##### Now, we will setup a remote between our code base and the heroku app we just made
---
```
heroku git:remote -a news_api
```

##### Now we need to set up our config variables for our Django app, go to your app and go into settings tab. Now, click on Reveal Config Variables and set the following variables
---
```
DISABLE_COLLECTSTATIC=1
DJANGO_ALLOWED_HOSTS=*
DJANGO_SETTINGS_MODULE=news_api.settings

# Now for safety purposes let's create a secret key from an online tool, https://miniwebtool.com/django-secret-key-generator/. This will help us create a new secure secret key. Next step, set this secret key in our Config Variables

SECRET_KEY="CREATED_SECRET_KEY"
```

##### Now, let's push the master branch to this app
----
```
git push heroku master
```

##### Now, let's link the database with Heroku PostgreSQL
----
```
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
# enter a username, password, and confirm password. This will be your first superuser which will help you enter the admin panel of Django
```

##### Now, the app is ready, go to the app URL, example -> https://hitori-newsapp.herokuapp.com/admin/. Now, sign in to the admin panel with the superuser you created in the last step.


