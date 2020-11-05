
#add necessary imports
#add routes
from flask import  render_template, request, url_for, abort
from . import main
from .fill_db import questionAnswerTuples
from .. import db
from ..models import Question
# from twilio import Twilio
from twilio.twiml.messaging_response import MessagingResponse

@main.route('/')
def index():
    return render_template('index.html')
@main.route('/student')
def student():
    return render_template('student.html')


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

# def questionAnswerTuples():
#     [("300 + 500? =\n A. 600\n B. 800\n C. 400\n D. 700\n","B","4","maths" ),
#     ("6.6 + 2.0? =\n A. 8.6\n B. 8.0\n C. 7.0\n D. 7.4\n"," A","4","maths" ),
#     ("56/7 =\n A. 0\n B. 8\n C. 7\n D. 9\n","8","4","maths" ),
#     ("3.146 kg = ______ g?=\n A. 3100\n B. 3200\n C. 3300\n D. 3146\n","D","4","maths" ),
#     ("__ + 8,700 = 9,000=\n A. 16700\n B. 300\n C. 2000\n D. 500\n","B","4","maths" ),

#     ("It is__________outside. Did you bring an umbrella?\n A. cold\n B. rainy\n C. windy\n D. sunny\n","B","4","English" ),
#     ("A person who is shy probably does NOT\n A. talk alot\n B. like animals\n C. have any friends\n D. get along with people\n","D","4","English" ),
#     ("What is the question?\n A. What are you doing?\n B. Where are you going?\n C. How have you been?\n D. Why are you so tired\n","D","4","English" ),
#     ("A____is coming, so temperatures will drop.A. cold front\n B. foggy day\n C. wind stom\n D. hurricane\n","B","4","English" ),
#     ("I would like another_________ of cake. A. piece\n B. peace\n C. peece\n D. peez\n","A","4","English" ),

#     ("Rocks are made of minerals\n A. True\n B. False\n C. I dont know\n D. no answer\n","A","4","Science" ),
#     ("When magma cools it forms igneous rock. Where is magma found?\n A. above ground\n B. underground\n C. on a mountain\n D. get along with people\n","D","4","Science" ),
#     ("What is the question?\n A. What are you doing?\n B. Where are you going?\n C. How have you been?\n D. on the outside of a volcano\n","B","4","Science" ),
#     ("Which phrase best completes the following sentence? The Hawaiian Islands were formed by________.\n.A. folding\n B. glaciers\n C. volcanoes\n D. faulting\n","C","4","Science" ),
#     ("What is the natural process that causes one kind of rock to change into another kind?\n A. weathering\n B. rock-cycle\n C. sediment\n D. metamorphic rock\n","A","4","English" ),

#     ("Dada zenu ni ______?\n A. ndefu\n B. waerevu\n C. werefu\n D. werevu\n","B","4","Kiswahili" ),
#     ("Sehemu ya juu zaidi za mlima ni\n A. upeo\n B. kilele\n C. ukungo\n D. kilima\n","D","4","Kiswahili" ),
#     ("Malipo atoayo mtu kusafiria ni\n A. nauli?\n B. mahari?\n C. nauri?\n D. kauri\n","D","4","Kiswahili" ),
#     ("Chakula cha mchana huitwa?\n A. cold front\n A. kiacha kinywa\n  B. kishuka\n C. ugali\n D. staftahi\n","B","4","Kiswahili" ),
#     ("Dada yake mama utamwita?\n A. mjomba\n B. halati\n C. shangazi\n D. wifi\n","A","4","Kiswahili" )
#     ]
