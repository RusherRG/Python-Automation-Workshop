from database import get_unpaid_participants
from mail import sendmail
from csv_fetch import read_csv
import json


def send_reminder(): 
    with open('config.json', 'r') as f:
        config = json.load(f)
    total_seats = config['total_seats']

    # unpaid, paid_count = get_unpaid_participants_from_csv()
    unpaid, paid_count = read_csv('participants.csv')
    print(total_seats, paid_count)
    for participant in unpaid:
        sendmail(to_email=participant[1], name=participant[0].split()[0].capitalize(),
                 seats_rem=total_seats-paid_count-23)

send_reminder()
