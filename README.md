# Workshop 6

In this workshop, we'll be introducing sub-resources and JWT authentication.

## Prerequisites

1. Install [Postman](https://www.postman.com/downloads/) - you don't need to create an account.

Postman is an awesome development tool to test our REST APIs.

2. Install [MongoDB Compass](https://www.mongodb.com/try/download/compass) - you don't need to create an account.

MongoDB Compass provides a simple GUI to view all MongoDB objects, which helps test whether our API works.

## Dependencies
Make sure to have these dependencies added to your project interpreter in PyCharm.

1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
2. [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
3. [flask-mongoengine](https://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
4. [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)

<b> Flask-JWT-Extended </b> is an open source Flask extension that provides JWT support.

## Changes

You'll notice that we have a new folder: authentication/ 

In order to make use of JWT authentication, we have added a User model, UserLogin and UserRegistration resources and corresponding UserService. Together, these enable a User to register and login to get a JWT token.

All requests to RiderResource (GET, POST, PATCH) now require a valid JWT token whose User.email matches Rider.email of the Rider object being accessed.

The reason to have User model separate from Rider model is for supporting Users who could be Riders, Drivers, etc. using a common User account. The field that ties User and Rider objects together is the shared email address.

Note that we don't save the actual password (still one of the #1 security blunders), but save a hashed version of it which is checked against the hashed-user-entered-password each time.

Trip model has been added, and can only be accessed as a sub-resource (GET, POST) of Rider.
