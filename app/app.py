from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
import csv
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ci491_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def index():
    usr_query = request.form.get('search_query')
    df = pd.read_csv('output.csv')
    myData = df[df['Specialty'].str.contains(str(usr_query), case=False)] 
    return render_template('home.html', usr_query=usr_query, myData=myData)


if __name__ == '__main__':
    app.run(debug=True)