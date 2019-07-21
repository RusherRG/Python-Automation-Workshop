from pymongo import MongoClient
import os
import datetime
mongodb_url = str(os.environ["CODECELL_CHATBOT_MONGODB"])


def connect():
    client = MongoClient(mongodb_url)
    db = client.python_automation
    return db


def get_all_participants():
    db = connect().participants
    return db.find()


def get_unpaid_participants():
    all_participants = list(get_all_participants())
    paid_count = 0
    unpaid = []
    now = datetime.datetime.now()
    for participant in all_participants:
        if participant['Payment'] == False:
            if (now - participant['time_filled']).seconds >= 12*60*60:
                unpaid.append(participant)
        else:
            paid_count += 1
    return unpaid, paid_count
