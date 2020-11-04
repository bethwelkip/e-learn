
from flask import render_template,request,redirect,url_for,abort
from . import main


@main.route('/')
def index():
    return render_template('student.html')


def receive_question():
    #Bethwel/Ronald
    # connect to twilio
    # connect to db
    # receive_question
    # find requested questions
    # reply with questions then with answers
    pass



def sign_up():
    # form to sign up
    # name, phone, grade
    # reach to db
    pass

# @main.route('/teacher/question')
# def submit_question():
#     #to implement later
#     #might have forgotten some stuff. please list here
#     pass