from flask import Flask, render_template,request,session
import csv
import random
from db import loguserup,signusersup,getname,addratingsfromuser
from RandomBookCovers import getcoversasjpg
import os
import secrets
import json
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ratingdisp')
def ratingdisp():
    return render_template('ratings.html')


@app.route('/login',methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if(loguserup(username,password)):
        name = getname(username)
        covers = getcoversasjpg()
        print(covers)
        session['username']=username
        session['userloggedin']=True
        return render_template('Loggedin.html',name=name, username=username,covers = covers)
    else:
        return 'err'

@app.route('/signup',methods=['POST'])
def signup():
    form = request.form
    name = form.get('name')
    username = form.get('username')
    password = form.get('password')
    signusersup(username,password,name)
    session['userloggedin'] = True
    book_covers = os.listdir('/Users/deepakkailash/PycharmProjects/BookStore/static/Bookcovers')


    return render_template('Loggedin.html',name=name)

@app.route('/randbooksuggest')
def randombooksuggestion():
    books = []
    with open('books.csv','r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            books.append(row)
        choice = random.choice(books)
    print(choice)
    return render_template('random_book.html',book=choice[0] ,author=choice[1])

@app.route('/addrating',methods=['POST'])
def addrating():
    if(session.get('userloggedin')==False or session.get('userloggedin')==None):
            return "Nope"
    else:
        values = request.get_json()
        bookname = values['bookname']
        username = session.get('username')
        rating = values['rating']
        print(bookname,username,rating)
        status = addratingsfromuser(username=username,bookname=bookname,rating=rating)
        response = dict()
        if(status==1):
            response['statusCode']=200
        elif(status==0):
            response['statusCode']=500

        return json.dumps(response)

if(__name__=='__main__'):
    app.run(debug=True)