#add necessary imports
#add routes
from flask import  render_template, request, url_for, abort
from . import main
from .fill_db import questionAnswerTuples
from .. import db
from ..models import Question
# from twilio import Twilio
from twilio.twiml.messaging_response import MessagingResponse
def index():
    #Dorcas: how would you like the front end
    pass

@main.route('/question', methods= ['POST'])
def receive_question():
    msg = request.form.get('Body').lower()
    user = request.form.get('From').lower()
    print(user)
    response = MessagingResponse()
    text = ["Welcome to E-Learn!\nThis is an online platform for you to study \
    from the comfort of your home!.\n To start us off, what subject would youlike to study today? Math, Science, Kiswahili or English?\n ", 
    "Invalid option :(.\nPlease select between the following options: Math, English, Kiswahili, Science"]
    subjects = ["math", "english", "science", "kiswahili", "cre", "social studies" ]
    resp = ""
    current_subject = ""
    if msg == "join egg-unusual" or msg == "hi":
        response.message(text[0])
    elif msg in subjects:
        print(msg)
        questions = Question.query.filter_by(subject = msg).all()
        current_subject = msg
        for question in questions:
            resp = resp + "\n" + question.question
        response.message(resp)
    elif msg == "done":
        questions = Question.query.filter_by(subject = "math").all()
        for question in questions:
            resp = resp + "\n" + question.answer
        response.message(resp)
    else:
        response.message(text[1])
    return str(response)


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