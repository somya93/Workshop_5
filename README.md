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

## Note

In order to avoid any model inconsistencies, please <b> delete </b> any existing database named <b> app-rest </b> using MongoDB Compass.

In Postman, once you have logged in (/login) and got an 'access_token', click 'Authorization' and paste the token in the text box with type set to 'Bearer Token'.

## Example Postman Requests

0. [GET] http://localhost:5000/rider
- This should throw an error due to missing JWT token.
1. [POST] http://localhost:5000/login?email=phil@cmu.org&password=phil
- Copy the access token in the JSON response and paste it into the 'Authorization' tab as a 'Bearer Token' type.
- Do not copy the "" double-quotes surrounding the long token string.
2. [GET] http://localhost:5000/rider
- This should return the rider details in JSON format. Copy the 'rider_id' value which is required in all subsequent steps.
3. [GET] http://localhost:5000/rider/rider_id
- Use the 'rider_id' value obtained from the earlier step, and you should get the same rider details.
4. [PATCH] http://localhost:5000/rider/rider_id?premium=true
- This should update the 'premium' field of the rider to 'true'.
5. [GET] http://localhost:5000/rider/rider_id/trip
- This should return an empty JSON list since we haven't created any trips yet.
6. [POST] http://localhost:5000/rider/rider_id/trip?fare=42
- This should create and return a trip object with 'fare' set to 42.
7. [GET] http://localhost:5000/rider/rider_id/trip
- This should return the trip that was just created in the earlier step.

Note that in each of the above steps (except the first 3 where we still didn't know the 'rider_id'), the 'rider_id' is required.
If the email fields of the Rider (with 'rider_id') and the User (from JWT 'access_token' during login/) don't match, you will get an error.
This ensures that only data corresponding to the currently logged-in User can be accessed (GET, POST, PATCH, etc.).