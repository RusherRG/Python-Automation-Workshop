from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from flask import render_template
import os
import sys

def sendmail(to_email, name, mail_type, seats_rem=0):
    
    from_email = ''
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Python Automation Workstop"
    msg['From'] = from_email
    msg['To'] = to_email
    
    if seats_rem:
        body = render_template('templates/{}.html'.format(mail_type),
                            'name':name,
                            'seats_rem': seats_rem,
                            'TITLE': "Reminder Email" if mail_type == 'remind' else 'Registration')
        content = MIMEText(body, 'html')
        msg.attach(content)
        response = {}
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as s:
                s.starttls()
                s.login(from_email, "grpizstmjcoxahos")
                print("Sending Mail")
                s.sendmail(from_email, to_email, msg.as_string())
            response['email_status'] = "Success"
        except Exception as err:
            print(err)
            response['email_status'] = "Failed"

        return response
