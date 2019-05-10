from flask import Flask, render_template, flash, request
from flask import render_template
import data.template as dt
from data.forms import myform
from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pusher import Pusher
import pusher
import requests, json, atexit, time, plotly
import json
import plotly.graph_objs as go
import numpy as np
import plotly
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from textML import textML
from dynamo import get_items

app = Flask(__name__)
title = "Offensive Comments Detection Based on YouTube Data."

# configure pusher object
pusher_client = pusher.Pusher(

)


# define variables for data retrieval
# times = []
# currencies = ["BTC"]
# prices = {"BTC": []}

times = []
c_number = []
t_number = []
def retrieve_data():

    pusher_client.trigger('my-channel', 'my-event', data)


@app.route("/")
def hello():
    return render_template('index.html', title=title)


@app.route('/query')
def query():
    form = myform(request.form)
    return render_template('query_index.html', title=title, form=form)  #, graphJSON=graphJSON)


@app.route('/query', methods=['POST'])
def check():
    global clean_toxic_probability
    global res
    text = request.form['search_key']
    textML_instance = textML()
    text, pos_neg, clean_toxic_probability = textML_instance.predict(text)
    if pos_neg[0] == 1:
        res = "Toxic"
    elif pos_neg[0] == 0:
        res = "Non-Toxic"
    else:
        res = "I don't know what happend?"
    rand_id = 1
    return render_template('disp.html', title=title,
                           sentence=text, rand_id=rand_id, res=res,
                           render_list=clean_toxic_probability)


@app.route('/analysis/<key>/<int:rand_id>')
def analysis(key, rand_id):
    #data = TwitterMain.get_analysis_data(key, rand_id)
    global clean_toxic_probability
    global res
    prob = list(clean_toxic_probability[0])
    # print(prob)
    return render_template('analysis.html', title=title,
                           res=res, data=prob)

@app.route('/graph')
def line():
    # create schedule for retrieving prices
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=retrieve_data,
        trigger=IntervalTrigger(seconds=5),
        id='retrieval_job',
        name='Retrieve streaming data every 5 seconds',
        replace_existing=True)
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

    return render_template('graph_pusher.html')  #, graphJSON=graphJSON)

if __name__ == "__main__":
    app.run()
    #app.run(host="localhost", port=8080)
