from flask import Flask, render_template, request, redirect
from sendEmail import send_email
import csv


def stor_info_into_database(data):
    i = 1
    with open('./database.txt', mode='a') as databasetxt:
        email = data['email']
        subject = data['subject']
        msg = data['mssg']
        databasetxt.write(
            "------------------------------------------------------")
        databasetxt.write(
            f'\nemail: {email} \nsubject: {subject} \nmessage: {msg} \n')
        i += 1


def stor_info_into_csv(data):
    with open('./database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["mssg"]
        csv_writer = csv.writer(
            database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            send_email(data['email'], data['subject'], data['mssg'])
            stor_info_into_database(data)
            stor_info_into_csv(data)
            return redirect('/submitted.html')
        except:
            return 'something is wrong please check your conx.'
    else:
        return 'Something went wrong. Please try again'
