from flask import  render_template, request, url_for, abort
from . import main
# from .fill_db import questionAnswerTuples
from .. import db
from ..models import Question
from .forms import quizForm
from twilio import Twilio
from twilio.twiml.messaging_response import MessagingResponse

@main.route('/')
def index():
    return render_template('index.html')

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

@main.route('/e-learn/Technicalsupport/', methods=['POST','GET'])
def exam_questions():
    form = quizForm()
    if form.validate_on_submit():
       subject= form.Subject.data
       question= form.Question.data
       answer = form.Answer.data 
       answers= (form.A.data, form.B.data,form.C.data, form.D.data)

       newquiz= Question(question=question, subject=subject,answer=answer)
