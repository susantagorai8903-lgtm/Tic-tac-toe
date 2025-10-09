from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    winner TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save_result', methods=['POST'])
def save_result():
    data = request.get_json()
    winner = data.get('winner', 'Draw')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO results (winner) VALUES (?)", (winner,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Result saved successfully!"})

@app.route('/history')
def history():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT winner, timestamp FROM results ORDER BY timestamp DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
