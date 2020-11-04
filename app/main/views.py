from flask import render_template,request,redirect,url_for,abort, flash, abort
from . import main
from .forms import  quizForm

#add necessary imports
#add routes

def index():
    #Dorcas: how would you like the front end
    pass


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

@main.route('/e-learn/Technicalsupport/', methods=['POST','GET'])
def exam_questions():
    form = quizForm()
    if form.validate_on_submit():
       Subject= form.Subject.data
       Answer = form.Answer.data 
       answers= (form.A.data, form.B.data,form.C.data, form.D.data)
