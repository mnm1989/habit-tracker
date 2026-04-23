# Habit Tracker 🧠✅

A simple **command-line habit tracker** built with Python.  
This project allows users to create habits, track daily progress, and view basic analytics.

The project is built with **clean architecture**, includes **automated tests**, and uses **GitHub Actions** for continuous integration.

---

## 🚀 Features

- Add new habits with a defined periodicity (e.g. daily)
- List all created habits
- Check off habits by date
- Store data persistently using JSON
- View basic analytics (streaks & progress – WIP)
- Automated tests with pytest
- CI pipeline with GitHub Actions

---

## 🛠️ Tech Stack

- **Python 3.12**
- **pytest** for testing
- **pytest-cov** for test coverage
- **GitHub Actions** for CI
- JSON-based storage

---

```## 📁 Project Structure
habit-tracker/
├── src/
│ ├── habit.py
│ ├── habit_manager.py
│ ├── analytics.py
│ ├── storage.py
│ └── main.py
│
├── tests/
│ ├── test_habits.py
│ ├── test_analytics.py
│ └── conftest.py
│
├── .github/
│ └── workflows/
│ └── tests.yml
│
├── .gitignore
└── README.md ```
## ▶️ Usage

## 🧪 Running Tests

Run all tests with coverage:

```bash
python -m pytest --cov=src
### 📦 Data Storage
Habits are persisted locally using a JSON file (`habits.json`) via a dedicated storage module.



