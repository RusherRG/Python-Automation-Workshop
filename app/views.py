from flask import render_template
from app import app
import requests
from flask import request
import datetime
import traceback
from app import database, passes, mail
from flask_cors import cross_origin

@app.route('/register', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    content = request.json
    content['time_filled'] = datetime.datetime.now()
    content['Payment'] = False
    # insert data to mongo
    if database.check_email(content['Email']):
        return 'Already Registered'

    try:
        passimg, content['Seat'] = passes.pass_gen(
            content['Name'], content['Email'], content['Payment'])
        mail.sendMail(content['Email'], content['Name'], passimg)
        database.add_participant(content)
    except:
        traceback.print_exc()
        return "Fail"

    # send confirmation mail
    return 'Registered Succesfully'
