from flask import Flask, request, jsonify
from pathlib import Path
import shutil
import sqlite3
import time

app = Flask(__name__)
INBOX = Path("inbox")
STORAGE = Path("cloud_api/storage")
STORAGE.mkdir(parents=True, exist_ok=True)
DB_PATH = "cloud_api/db.sqlite"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
conn.execute('''CREATE TABLE IF NOT EXISTS documents
                (id INTEGER PRIMARY KEY, name TEXT, label TEXT, timestamp TEXT)''')
conn.commit()

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    label = request.form['label']
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    dest = STORAGE / file.filename
    file.save(dest)
    conn.execute("INSERT INTO documents (name, label, timestamp) VALUES (?, ?, ?)",
                 (file.filename, label, timestamp))
    conn.commit()
    return jsonify({"status": "success", "file": file.filename, "label": label})

@app.route("/docs", methods=["GET"])
def docs():
    cursor = conn.execute("SELECT * FROM documents ORDER BY timestamp DESC")
    results = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)