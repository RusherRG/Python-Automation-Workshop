from csv_fetch import read_csv, write_csv
from mail import sendmail
import json


def send_reminder():
    with open('config.json', 'r') as f:
        config = json.load(f)
    total_seats = config['total_seats']
    unpaid, paid_count = read_csv('data.csv')
    for participants in unpaid:
        sendmail(to_email=participants[1], name=participants[0], mail_type='remind', seats_rem=total_seats-paid_count)


send_reminder()
