from database import get_unpaid_participants
from mail import sendmail
import json


def send_reminder(): 
    with open('config.json', 'r') as f:
        config = json.load(f)
    total_seats = config['total_seats']

    unpaid, paid_count = get_unpaid_participants()
    for participant in unpaid:
        sendmail(to_email=participant['Email'], name=participant['Name'],
                 seats_rem=total_seats-paid_count)


send_reminder()
