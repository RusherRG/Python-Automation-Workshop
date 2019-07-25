
from mail import sendmail
from csv_fetch import read_csv
import json


def send_reminder():
    with open('config.json', 'r') as f:
        config = json.load(f)
    total_seats = config['total_seats']

    # unpaid, paid_count = get_unpaid_participants_from_csv()
    unpaid, paid_count = read_csv('test.csv')
    print(total_seats, paid_count)
    for participant in unpaid:
        sendmail(to_email=participant[1], name=participant[0].split()[0].capitalize(),
                 seats_rem=37)
        if participant[0].split()[0].capitalize() == 'Neel':
            input()
send_reminder()
