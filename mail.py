from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from jinja2 import Environment, FileSystemLoader
import datetime
import os
import sys


def sendmail(to_email, name, seats_rem=0):

    from_email = str(os.environ.get("SENDER_EMAIL"))
    forwarder = str(os.environ.get("FORWARDER_EMAIL"))
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Payment Reminder"
    msg['From'] = forwarder
    msg['To'] = to_email

    if seats_rem:
        body = _render_template(name=name, num_seats=seats_rem)
        content = MIMEText(body, 'html')
        msg.attach(content)
        FROMADDR = "%s <%s>" % ('KJSCE CodeCell', forwarder)
        response = {}
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as s:
                s.starttls()
                s.login(from_email, "grpizstmjcoxahos")
                print("Sending Mail")
                s.sendmail(FROMADDR, to_email, msg.as_string())
            response['email_status'] = "Success"
        except Exception as err:
            print(err)
            response['email_status'] = "Failed"

        return response


def _render_template(name, num_seats):
    file_loader = FileSystemLoader('templates')
    env = Environment(
        loader=file_loader,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    template = env.get_template('remind.html')
    template.globals['now'] = datetime.datetime.utcnow
    return template.render(name=name, num_seats=num_seats)
