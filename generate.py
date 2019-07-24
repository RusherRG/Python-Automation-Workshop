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
    template = env.get_template('template.html')
    return template.render(csv_data=csv_data)


def generate_template(data):
    csv_data = []
    for row in data:
        data_dict = {
            'name': row[0],
            'phone': row[1],
            'dob': row[2],
            'city': row[3],
            'email': row[4],
            'payment': row[5],
        }
        csv_data.append(data_dict)
    generated = _render_template(csv_data=csv_data)
    with open('templates/index.html', 'w') as index_html:
        index_html.write(generated)

    return generated
