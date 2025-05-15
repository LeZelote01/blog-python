from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialiser la base de données SQLite
def init_db():
    with sqlite3.connect("blog.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)
        # Article de test
        conn.execute("INSERT OR IGNORE INTO articles (title, content, date) VALUES (?, ?, ?)",
                     ("5 Scripts Python pour Automatiser Vos Tâches",
                      "Apprenez à renommer des fichiers en masse :<br><pre><code>import os\nfor i, f in enumerate(os.listdir('dossier'), 1):\n    os.rename(f, f'fichier_{i}.pdf')</code></pre><p>Obtenez la version complète pour 5€ sur <a href='ko-fi.com/lezelote'>Ko-fi</a>.</p>",
                      "2025-05-15"))
        conn.commit()

@app.route('/')
def index():
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.execute("SELECT id, title, date FROM articles ORDER BY date DESC")
        articles = cursor.fetchall()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:id>')
def article(id):
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.execute("SELECT title, content, date FROM articles WHERE id = ?", (id,))
        article = cursor.fetchone()
    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)