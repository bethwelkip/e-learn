
from flask import  render_template, request, url_for, abort, redirect,flash
from . import main
from .fill_db import questionAnswerTuples
from .. import db
from ..models import Question,Answer, Admin, Student
from .forms import quizForm, loginForm, RegistrationForm
from twilio.twiml.messaging_response import MessagingResponse

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/student')
def student():
    return render_template('student.html')

@main.route('/question', methods= ['POST'])
def receive_question():
    if not Question.query.filter_by(seen = False).all():
        questionAnswerTuples()
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
        questions = Question.query.filter_by(subject = msg).all()
        if not questions:
            response.message(f"We currently don't have any questions for the subject {msg}. Check back in a day or two.")
        else:
            if len(questions)>5:
                questions = questions[0:5]
            for question in questions:
                question.seen = True
                db.session.commit()
                resp = resp + "\n" + question.question
            response.message(resp)
    elif msg.lower() == "done":
        questions = Question.query.filter_by(seen = True).all()
        print(questions)
        for question in questions:
            question.seen = False
            db.session.commit()
            answer = Answer.query.filter_by(question_id = question.question_id).first()
            resp = resp + "\n" + answer.answer
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
       question = form.question.data + "\n" + "A. "+ form.A.data + "\n" + "B. "+ form.B.data + "\n" + "C. "+ form.C.data + "\n" + "D. "+ form.C.data + "\n"
       newQuiz = Question(question = question,subject = subject,grade = grade)
       db.session.add(newQuiz)
       db.session.commit()
       question = Question.query.filter_by(question = question).first()
       newAnsw = Answer(answer = answer,question_id =question.question_id )
       db.session.add(newAnsw)
       db.session.commit()
       return redirect(url_for('main.exam_questions'))
    return render_template('questions.html',form = form)
@main.route('/e-learn/login/', methods=['POST', 'GET'])
def login():
    form= loginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(email= form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.exam_questions'))
        flash ('Invalid username or password')
    return render_template('login.html', form=form)
@main.route('/e-learn/signup', methods=['POST', 'GET'])
def signUp():
    form= RegistrationForm()
    if form.validate_on_submit():
        user = Student(name=form.name.data, phone=form.mobile_phone.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.student'))  
    return render_template('signup.html', form= form)

# @main.route('/teacher/question')
# def submit_question():
#     #to implement later
#     #might have forgotten some stuff. please list here
#     pass
