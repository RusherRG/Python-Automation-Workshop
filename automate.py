import csv
import random
import os
from jinja2 import Environment, FileSystemLoader
from faker import Faker


def generate_random_data(count):
    fake_it = Faker()
    fake_data = []
    for _ in range(random.randint(1, 20)):
        fake = [
            fake_it.name(),
            fake_it.date(),
            "pyauto{}@yopmail.com".format(str(count+_)),
            random.choice([fake_it.city(), ""]),
            random.choice([fake_it.phone_number(), ""]),
            "unpaid"
        ]
        fake_data.append(fake)
    return fake_data


def read_csv():
    with open("/home/rusherrg/CodeCell/Python-Automation-Workshop/data.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        for row in csv_reader:
            data.append(row)

    return data


def write_csv(data, write_type):
    with open("/home/rusherrg/CodeCell/Python-Automation-Workshop/data.csv", write_type) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for row in data:
            csv_writer.writerow(row)


def _render_template(data):
    file_loader = FileSystemLoader('/home/rusherrg/CodeCell/Python-Automation-Workshop/templates')
    env = Environment(
        loader=file_loader,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    template = env.get_template('template.html')
    return template.render(data=data)


def random_paid(data):
    for row in data:
        if row[-1] == "unpaid" and random.randint(0, 2) == 1:
            row[-1] = "paid"
    return data


def preprocess(data):
    data_dict = []
    for row in data:
        data_dict.append({
            "name": row[0],
            "dob": row[1],
            "email": row[2],
            "city": row[3],
            "phone": row[4],
            "payment": row[5],
        })
    return data_dict


def run():
    print("Randomizing paid info")
    data = read_csv()
    data = random_paid(data)
    write_csv(data, "w")

    print("Generating Fake data")
    data = generate_random_data(len(data))
    write_csv(data, "a")

    print("Preprocess data")
    data = read_csv()
    data = preprocess(data)

    print("Rendering HTML")
    html = _render_template(data)
    with open('/home/rusherrg/CodeCell/Python-Automation-Workshop/templates/index.html', 'w') as f:
        f.write(html)

    print("Pushing to surge")
    os.system("surge /home/rusherrg/CodeCell/Python-Automation-Workshop/templates/ automatescrape.surge.sh")

    print("Success")


run()
