from flask import render_template
from app import app
import requests
from flask import request
import datetime
from app import database, passes, mail
from flask_cors import cross_origin

@app.route('/register', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    content = request.json
    content['payment'] = False
    content['time_filled'] = str(datetime.datetime.now().time())

    try:
        passimg = passes.pass_gen(
            content['Name'], content['Email'], content['payment'])
        mail.sendMail(content['Email'], content['Name'], passimg)
    except Exception as exc:
        print(exc)
        return "Fail"

    # insert data to mongo
    if not database.add_participant(content):
        return 'Fail'

    # send confirmation mail
    return 'Registered Succesfully'
