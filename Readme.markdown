# FreshTomatoes - A movie review App [using django rest framework and angular js / angular material

## Dependencies

To setup and run the sample code, you're going to need `npm` from NodeJS available to install the frontend code.

## Setup

You're encouraged to setup a `virtualenv` to work in prior to configuring the dependencies.

1. Install Python Requirements

        pip install -r requirements.txt
        python setup.py develop

2. Install Bower + Grunt

		npm install -g grunt-cli bower

3. Install Assets

        npm install
        bower install

5. Setup the Database

        make create_database; make make_fixtures

6. Run the Server

        ./manage.py runserver



The super user / admin user login is:

superuser / test123

URL
http://127.0.0.1/movies

Known issues:

1. The edit functionality does doesnt work - there's seems to be an issue passing scope variables between different controllers in angular material. 
