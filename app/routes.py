from flask import render_template, request, redirect
from app import app

x = []
@app.route('/')
def index():
    x.clear()
    print(x)
    return render_template('home.html')

@app.route('/q1', methods=['GET', 'POST'])
def q1():
    print(request.method)
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 3:
            x.append(["q1", "correct", "The correct answer was 3: Trees make the air cleaner"])
        else:
            x.append(["q1", "wrong", "The correct answer was 3 Trees make the air cleaner"])
        print(x)
        return redirect('/q2')
    return render_template('q1.html', x=x)

@app.route('/q2', methods=['GET', 'POST'])
def q2():
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 1:
            x.append(["q2", "correct", "The correct answer was 1: Seed, Tree, Apple"])
        else:
            x.append(["q2", "wrong", "The correct answer was 1: Seed, Tree, Apple"])
        print(x)
        return redirect('/q3')
    return render_template('q2.html', x=x)

@app.route('/q3', methods=['GET', 'POST'])
def q3():
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 1:
            x.append(["q3", "correct", "The correct answer was 1: Everyday"])
        else:
            x.append(["q3", "wrong", "The correct answer was 1: Everyday"])
        return redirect('/q4')
    return render_template('q3.html', x=x)

@app.route('/q4', methods=['GET', 'POST'])
def q4():
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 3:
            x.append(["q4", "correct", "The correct answer was 3: Fall"])
        else:
            x.append(["q4", "wrong", "The correct answer was 3: Fall"])
        print(x)
        return redirect('/q5')
    return render_template('q4.html', x=x)

@app.route('/q5', methods=['GET', 'POST'])
def q5():
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 2:
            x.append(["q5", "correct", "The correct answer was 2: Turkey"])
        else:
            x.append(["q5", "wrong", "The correct answer was 2: Turkey"])
        print(x)
        return redirect('/results')
    return render_template('q5.html', x=x)

@app.route('/results')
def results():
    score = 0
    comment = ""
    new_scores = x
    for result in x:
        if result[1] == 'correct':
            score += 1
    if score == 0:
        comment = "Great job for trying."
    elif score == 1:
        comment = "One out of five! That's awsome!"
    elif score == 2:
        comment = "Two out of Five! That is really really good!"
    elif score == 3:
        comment = "Three out of Five! I never thought anyone would do this well!"
    elif score == 4:
        comment = "Four out of Five! I wish I could swear, becuase I am blown away!"
    elif score == 5:
        comment = "Oh my goodness! This is the most impressive thing I have ever seen, and I once saw a Lionel Richie Concert!"
    return render_template('results.html', x=new_scores, score=score, comment=comment)
x = []