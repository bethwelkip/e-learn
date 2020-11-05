from flask import  render_template, request, url_for, abort, redirect
from . import main
# from .fill_db import questionAnswerTuples
from .. import db
from ..models import Question,Answer, Admin, Student
from .forms import quizForm, loginForm, RegistrationForm
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
       answer = form.Answer.data 
       grade = form.Grade.data
       question = form.question.data + "\n" + "A"+ form.A.data + "\n" + "B"+ form.B.data + "\n" + "C"+ form.C.data + "\n" + "D"+ form.C.data + "\n"
       newQuiz = Question(question = question,subject = subject,grade = grade)
       db.session.add(newQuiz)
       db.session.commit()
       newAnsw = Answer(answer = answer)
       db.session.add(newAnsw)
       db.session.commit()
       return redirect(url_for('main.exam_question'))
    return render_template('template')
@main.route('/e-learn/login/', methods=['POST', 'GET'])
def login():
    form= loginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(email= form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.exam_questions'))
        flash ('Invalid username or password')
    return render_template('template', form=form)
@main.route('/e-learn/signup', methods=['POST', 'GET'])
def signUp():
    form= RegistrationForm()
    if form.validate_on_submit():
        user = Student(name=form.name.data, phone=form.mobile_phone.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.student'))

    return render_template('template', form= form)

