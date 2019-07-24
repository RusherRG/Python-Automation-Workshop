from scrape import scraper
from csv_utils import read_csv, write_csv, get_unpaid_participants
from generate import generate_template
from mail import sendmail
import json

# data = scraper('http://csvdata.surge.sh/')
# for info in data:
#     write_csv(info.values(), "studentdetails.csv")

# unpaid_participants, paid_count = get_unpaid_participants("studentdetails.csv")

# with open('config.json', 'r') as f:
#     config = json.load(f)
# total_seats = 500

data = read_csv("studentdetails.csv")
template = generate_template(data)

# for participant in unpaid_participants:
#     sendmail(to_email=participant[0], html=template)
