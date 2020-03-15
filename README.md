# Ze Delivery 

Backend Challenge Python 3.6.7 REST project 

## Getting Started

The service is already running and working on heroku and if you are feeling anxious and can not wait to see the amazing magic of an ApiREST with your own eyes.
you can [Check api documentation here](https://documenter.getpostman.com/view/10728918/SzS2x8Pz?version=latest#131a6529-7529-4444-81e8-92cdf5c7ef2b).

it would be better if you have [postman](https://dl.pstmn.io/download/latest/osx) installed.
to run it you can click on: 

![asdf](https://github.com/sebastianhe-jpg/ze-delivery-backend/blob/develop/img.png "downdload ")

and follow the steps.

Otherwise if you are still reading this, let me tell you a little bit more about the project. 

this repo reponses to [this Backend Challenge](https://github.com/ZXVentures/ze-code-challenges/blob/master/backend.md) 

The application is running in Python 3.6.7 and uses the web microframework and uses (at the moment) no-sql db MongoDB

[Download Python 3.6.7](https://www.python.org/downloads/release/python-367/)
 
[Download Flask](https://www.python.org/downloads/release/python-367/)
 
[Create MongoDb account](https://www.mongodb.com/)


## Deployment

on the terminal of your local machine write
```
git clone https://github.com/sebastianhe-jpg/ze-delivery-backend.git
```
go to the repo folder and install dependencies
```
pip install -r requirements.txt
```

then go to the mods folder

```
cd mods/
```
and create the .env file
```
vi .env
```
inside the .env file write the following
(note that you should create the mongo collection first and get the mongourl from there)
```
LOCAL_PATH = ''

MONGO_URL = ''
MONGO_DB = 'ze-delivery'
MONGO_COL = 'pdvs'
```
finally you should go to you repo root folder and write
```
python app.py
```
and the console should print something like this
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
then [Check api documentation] in the beginning


## Authors
* **Sebastian He** - *Initial work* - [sebastianhe-jpg](https://github.com/sebastianhe-jpg)
