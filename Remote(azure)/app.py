from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/homepage')
def homepage():
    return 'This is the home page'

@app.route('/patientportal')
def patientportal():
    return 'This is the patient portal page'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

##sudo nohup python3 app.py > log.txt 2>&1 & 
# to run the application in the background even when the terminal is closed   