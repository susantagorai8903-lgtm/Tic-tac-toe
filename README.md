# Tic-tac-toe
# 🎮 Tic Tac Toe — Fullstack (Flask + Browser Frontend)

## 📌 Overview
This repository contains a small fullstack Tic Tac Toe project. It includes a Flask backend that stores match results in an SQLite database and a browser frontend (HTML/CSS/JavaScript) that lets two players play locally in the browser. The original project used PyScript for client-side logic; the current version uses a plain JavaScript frontend to ensure reliable interaction and compatibility.

## 🧱 Project structure
```
Tic Tac toe /
│
├── app.py                   # Flask app and endpoints (/, /save_result, /history)
├── database.db              # SQLite DB (created automatically)
├── templates/
│   └── index.html           # Main HTML (game board + JS frontend)
├── static/
│   ├── style.css            # Styles for the game
│   └── game_logic.py        # (optional) PyScript source (kept for reference)
├── scripts/
│   └── test_endpoints.py    # Simple script to test /save_result and /history
└── README.md                # This file
```

## 🚀 How to run (development)
1. Create a virtual environment (recommended):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```
2. Install dependencies:
```powershell
pip install flask
```
3. Run the app:
```powershell
python app.py
```
4. Open your browser at:

http://127.0.0.1:5000

Notes:
- The SQLite database file `database.db` is created automatically on first run.
- The frontend logic is implemented in `templates/index.html` using plain JavaScript so it works in any modern browser.

## ⚙️ Features
- Two-player Tic Tac Toe played locally in the browser (X and O alternate turns)
- Win/draw detection in the browser
- Game results are sent to the server and persisted in SQLite (`/save_result`)
- `/history` endpoint returns the most recent matches (last 10)
- `scripts/test_endpoints.py` can be used to programmatically test the backend

## 🔧 Test endpoints (quick)
Run the small test script to POST a test result and fetch history:
```powershell
python scripts\test_endpoints.py
```

## ♻️ Future enhancements
- Add a user system and leaderboard (store player names and aggregate stats)
- Implement an AI opponent (minimax algorithm or a simple heuristic)
- Add visual highlights for the winning combination and disable board after game over
- Add automated tests (pytest) for backend endpoints and add CI
- Improve UI/UX (animations, mobile responsiveness, better accessibility)

---
