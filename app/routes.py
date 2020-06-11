from flask import render_template, request, redirect
from app import app

correct_answers = {
    1 : "The correct answer was 3: Trees make the air cleaner",
    2 : "The correct answer was 1: Seed, Tree, Apple",
    3 : "The correct answer was 1: Everyday",
    4 : "The correct answer was 3: Fall",
    5 : "The correct answer was 2: Turkey",
    6 : "The correct answer was 4: Age got nothing to do with. Everyone should care!",
    7 : "The correct answer was 5: A vital part of the aquatic food chain",
}
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/q1', methods=['GET', 'POST'])
def q1():
    score = ''
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 3:
            score = '1'
        else:
            score = '0'
        return redirect(f'/q2?score={score}')
    return render_template('q1.html')

@app.route('/q2', methods=['GET', 'POST'])
def q2():
    if not request.args.get('score'):
        return redirect('/')
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 1:
            score = request.args['score'] + '1'
        else:
            score = request.args['score'] + '0'
        return redirect(f'/q3?score={score}')
    return render_template('q2.html')

@app.route('/q3', methods=['GET', 'POST'])
def q3():
    if not request.args.get('score'):
        return redirect('/')
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 1:
            score = request.args['score'] + '1'
        else:
            score = request.args['score'] + '0'
        return redirect(f'/q4?score={score}')
    return render_template('q3.html')

@app.route('/q4', methods=['GET', 'POST'])
def q4():
    if not request.args.get('score'):
        return redirect('/')
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 3:
            score = request.args['score'] + '1'
        else:
            score = request.args['score'] + '0'
        return redirect(f'/q5?score={score}')
    return render_template('q4.html')

@app.route('/q5', methods=['GET', 'POST'])
def q5():
    if not request.args.get('score'):
        return redirect('/')
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 2:
            score = request.args['score'] + '1'
        else:
            score = request.args['score'] + '0'
        return redirect(f'/q6?score={score}')
    return render_template('q5.html')

@app.route('/q6', methods=['GET', 'POST'])
def q6():
    if not request.args.get('score'):
        return redirect('/')
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 4:
            score = request.args['score'] + '1'
        else:
            score = request.args['score'] + '0'
        return redirect(f'/q7?score={score}')
    return render_template('q6.html')

@app.route('/q7', methods=['GET', 'POST'])
def q7():
    if not request.args.get('score'):
        return redirect('/')
    if request.method == 'POST':
        y = request.form['answer']
        if int(y) == 5:
            score = request.args['score'] + '1'
        else:
            score = request.args['score'] + '0'
        return redirect(f'/results?score={score}')
    return render_template('q7.html')

@app.route('/results')
def results():
    if not request.args.get('score'):
        return redirect('/')
    score = 0
    for i in request.args['score']:
        score += int(i)
    comment = ""
    if score == 0:
        comment = "Great job for trying."
    elif score == 1:
        comment = "One out of seven! That's awesome!"
    elif score == 2:
        comment = "Two out of seven! That is really really good!"
    elif score == 3:
        comment = "Three out of seven! I never thought anyone would do this well!"
    elif score == 4:
        comment = "Four out of seven! I wish I could swear, because I am blown away!"
    elif score == 5:
        comment = "Oh my goodness! This is the most impressive thing I have ever seen, and I once saw a Lionel Richie Concert!"
    elif score == 6:
        comment = "Everytime the number 6 is used, you owe Drake a royalty fee of $2.24, so while this is a good score, it will cost you."
    elif score == 7:
        comment = "Perfect score! The environment is saved!"
    return render_template('results.html', score=score, comment=comment)
