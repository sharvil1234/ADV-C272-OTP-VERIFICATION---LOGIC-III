# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC5ef4934056675c2b55cf5716bd5b11b9'
        auth_token = '69143701261a279cec4a449a83f7dfdf'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VAa08dc3556a8c3ed6a3e72826729e529b') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'AC5ef4934056675c2b55cf5716bd5b11b9'
    auth_token = '69143701261a279cec4a449a83f7dfdf'
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
        .services('VAa08dc3556a8c3ed6a3e72826729e529b') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')
    else:
        return redirect("https://collaborative-document-3fgz.onrender.com")


if __name__ == "__main__":
    app.run()