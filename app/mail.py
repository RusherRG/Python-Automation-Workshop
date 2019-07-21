import getpass as gp
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from flask import render_template


def sendMail(email, name, ImgFileName):
    smtp_server = "smtp.gmail.com"
    port = 587
    # Enter sender and reviever emails below
    sender = str(os.environ.get('SENDER_EMAIL'))
    forwarder = str(os.environ.get('FORWARDER_EMAIL'))
    # Sender mail should have less secure apps enabled or use app password
    reciever = email

    txt = MIMEMultipart("alternative")

    # Specify subject of mail, sender and reciever
    txt["Subject"] = "Workshop registration ACK"
    txt["From"] = forwarder
    txt["To"] = reciever

    # Content of the mail to be sent
    str1 = render_template('register.html',name=name)
    str1 = MIMEText(str1, "html")
    txt.attach(str1)
    
    # This example assumes the image is in the current directory
    fp = open('app/static/passes/'+ImgFileName, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    txt.attach(msgImage)

    # Input password from user
    password = str(os.environ.get('APP_PASSWD'))
    con = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    FROMADDR = "%s <%s>" % ('KJSCE CodeCell', forwarder)

    server.starttls()
    server.login(sender, password)
    # Spam people :P
    # for reciever in recievers:
    server.sendmail(FROMADDR, reciever, txt.as_string())
