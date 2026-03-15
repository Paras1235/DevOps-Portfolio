import requests
import sqlite3
import os
import sqlite3
import requests
from flask import Flask, render_template, request, redirect, send_from_directory
# This tells Flask exactly where to find your 'static' folder
app = Flask(__name__, static_folder='static')
NEWS_API_KEY = '709559f1359f4dbdadd243b382a14f55'

# We use a global connection for the :memory: database so it stays alive
# while the app is running.
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

    # Fetch skills from Memory
    c = db.cursor()
    c.execute('SELECT name FROM skills')
    db_skills = [row[0] for row in c.fetchall()]

    # Default skills if none added yet
    skills = db_skills if db_skills else ["Python", "Flask", "Docker"]

    # Fetch News
    articles = []
    try:
        url = f'https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={NEWS_API_KEY}'
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            articles = r.json().get('articles', [])[:6]
    except:
        pass

    return render_template('index.html', skills=skills, articles=articles)

if __name__ == "__main__":
    from flask import send_from_directory
import os

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))    app.run(host="0.0.0.0", port=5000, debug=True)