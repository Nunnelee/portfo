from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/djn.html')
def djn():
    return render_template('djn.html')

@app.route('/germany.html')
def germany():
    return render_template('germany.html')

@app.route('/doggos.html')
def doggos():
    return render_template('doggos.html')  

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return "Thank you! I'll contact you soon."
    else:
        return 'something went wrong. Try again.'

