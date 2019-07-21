from pymongo import MongoClient
import os
mongodb_url = str(os.environ["CODECELL_CHATBOT_MONGODB"])


def connect():
    client = MongoClient(mongodb_url)
    db = client.python_automation
    return db


def check_email(email):
    db = connect().participants
    if db.find_one({'Email': email}):
        return 1
    return 0


def add_participant(participant):
    db = connect().participants
    participant['Payment'] = False
    db.insert(participant)
    return 1
