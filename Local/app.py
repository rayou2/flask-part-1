from flask import Flask

app = Flask(__name__)

@app.route('/') ## would leave the / for it to nagivate to the default page
def hello_world():
    return 'Hello world!'

@app.route('/homepage')
def homepage():
    return 'This is the home page'

@app.route('/patientportal')
def patientportal():
    return 'This is the patient portal page'
## here it would be able to nagivate to the other pages with /"name"


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)