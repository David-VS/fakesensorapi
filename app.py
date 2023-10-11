from flask import Flask
from datetime import datetime
from model import measurements as m
import random

app = Flask(__name__)

# als je timestamps uit datums wilt halen, er bestaan convertors
# https://www.epochconverter.com
data = [
                m.Measurement(12),
                m.Measurement(23, datetime.fromtimestamp(1617295943.17321)),
                m.Measurement(20.5, datetime.fromtimestamp(1697017737))
                ]



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/current')
def make_current():
    temp = random.randint(-20, 40)
    new_m = m.Measurement(temp)
    data.append(new_m)
    return 'success'


@app.route('/all')
def show_all():
    return data


@app.route('/avg')
def show_avg():
    total_temp = 0
    total_entries = len(data)

    for entry in data:
        total_temp += entry.temperature

    result = total_temp / total_entries
    return str(result)


if __name__ == '__main__':
    app.run()
