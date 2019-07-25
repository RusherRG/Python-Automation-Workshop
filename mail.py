from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from jinja2 import Environment, FileSystemLoader
import datetime
import os
import sys


def sendmail(to_email, name, seats_rem=0):

    from_email = "codecell.engg@somaiya.edu"
    forwarder = "workshop@kjscecodecell.com"
    msg = MIMEMultipart('alternative')
    msg['Label'] = "Python-Automation"
    msg['Subject'] = "Last Call for Automation Workshop"
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
                s.sendmail(FROMADDR, to_email, msg.as_string())
                print(f"Reminder Mail sent to {name}")
            response['email_status'] = "Success"
        except Exception as err:
            # print(err)
            print(f'Could not send mail to {name}')
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
    return template.render(name=name, num_seats=num_seats)
