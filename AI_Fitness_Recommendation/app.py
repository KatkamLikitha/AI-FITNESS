from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd
from utils.recommendation import get_recommendation

app = Flask(__name__)
model = pickle.load(open('model/fitness_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('recommend'))
    return render_template('register.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        goal = request.form['goal']
        user_data = pd.DataFrame([[age, weight, height, goal]], columns=['Age','Weight','Height','Goal'])
        recommendations = get_recommendation(user_data, model)
        return render_template('recommendations.html', recommendations=recommendations)
    return render_template('recommendations.html', recommendations=None)

if __name__ == '__main__':
    app.run(debug=True)