import os
from app import app
from flask import render_template, request, redirect

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

app.config['MONGO_URI'] = 'mongodb+srv://admin:OABPGgj8pUzC3Zlj@cluster0-jeuyz.mongodb.net/test?retryWrites=true&w=majority'


mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():

    collection = mongo.db.Events
    Events = list(collection.find({}))

    return render_template('index.html', Events = Events)



@app.route('/input')
def input():
    return render_template('input.html')
    # going to display the input.html file

# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    test = mongo.db.test
    test.insert({'name'})
    # insert new data

    # return a message to the user
    return "Added data to data base"


@app.route('/results', methods = ['get', 'post'] )

def results():
    userdata = dict(request.form)

    event_date = userdata['Event Date']
    event_name = userdata['Event Name']


    Events = mongo.db.Events
    Events.insert({'event_date': event_date, 'event_name': event_name})
    Events = list(Events.find({}))


    return render_template('index.html', Events = Events)


@app.route('/deleteAll')
def deleteAll():

    collection = mongo.db.Events


    collection.delete_many({})


    return ""











    # return userdata
