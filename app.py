import os
import sqlite3
import requests
from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__, static_folder='static')
NEWS_API_KEY = '709559f1359f4dbdadd243b382a14f55'

# We use a global connection for the :memory: database
db = sqlite3.connect(':memory:', check_same_thread=False)

def init_db():
    c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS skills (id INTEGER PRIMARY KEY, name TEXT)')
    db.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        new_skill = request.form.get('skill')
        if new_skill:
            c = db.cursor()
            c.execute('INSERT INTO skills (name) VALUES (?)', (new_skill,))
            db.commit()
        return redirect('/')
    
    c = db.cursor()
    c.execute('SELECT name FROM skills')
    db_skills = [row[0] for row in c.fetchall()]
    skills = db_skills if db_skills else ["Python", "Flask", "Docker"]
    
    articles = []
    try:
        r = requests.get(f'https://newsapi.org/v2/top-headlines?category=technology&apiKey={NEWS_API_KEY}')
        if r.status_code == 200:
            articles = r.json().get('articles', [])[:6]
    except:
        pass
    
    return render_template('index.html', skills=skills, articles=articles)

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))