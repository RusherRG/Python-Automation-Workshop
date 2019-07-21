from flask import render_template
from app import app
import requests
from flask import request
import datetime
from app import database, passes, mail


@app.route('/register', methods=['POST'])
def register():
    content = request.json
    content['payment'] = False
    content['time_filled'] = str(datetime.datetime.now().time())

    # insert data to mongo
    if database.check_email(content['Email']):
        return 'Already Registered'

    try:
        passimg = passes.pass_gen(
            content['Name'], content['Email'], content['payment'])
        mail.sendMail(content['Email'], passimg)
        database.add_participant(content)

    except Exception as exc:
        print(exc)
        return "Fail"

    # send confirmation mail
    return 'Registered Succesfully'
