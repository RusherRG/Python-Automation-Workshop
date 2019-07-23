from jinja2 import Environment, FileSystemLoader
import csv

def _render_template(csv_data):
    file_loader = FileSystemLoader('templates')
    env = Environment(
        loader=file_loader,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    template = env.get_template('gen_temp.html')
    return template.render(csv_data = csv_data)

with open('studentdetails.csv') as csv_file:
    csv_data = []
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            csv_data.append(
                {
                    'name': row[0],
                    'phone': row[1],
                    'dob': row[2],
                    'city':row[3],
                    'email': row[4]
                }
            )
            line_count += 1
    
    generated = _render_template(csv_data = csv_data)
    with open('index.html', 'w') as index_html:
        index_html.write(generated)



