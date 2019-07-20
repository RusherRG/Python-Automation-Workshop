from flask import render_template
from app import app
import requests
from flask import request
import datetime

@app.route('/register',methods=['POST'])
def register():
    content = request.json
    content['payment'] = False
    content['time_filled'] = datetime.datetime.now().time()
    # insert data to mongo
    # send confirmation mail
    return 'Registered Succesfully'