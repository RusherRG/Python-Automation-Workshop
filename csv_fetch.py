import csv

def read_csv(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        unpaid = []
        paid_count = 0
        for row in csv_reader:
            if row[-1]=='unpaid':
                unpaid.append(row)
            else:
                paid_count += 1
    return unpaid, paid_count


def write_csv(data, filename):
    with open(filename) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(data)

