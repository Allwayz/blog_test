from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
https://timetables.cardiff.ac.uk/ical?61f1d5db&group=false&eu=YzIxMDI4NzEy&h=GY60rPNNY62nrjLvRo1mQNcJpnUodZL4xz_nwSi2eU4=
