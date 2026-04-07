# 🃏 Blackjack Game (Python)

## 📌 Overview

A command-line implementation of the classic **Blackjack** card game, simulating gameplay between a user and a computer dealer.

This project focuses on modelling real game rules and managing dynamic game state using clean, modular Python code.

---

## 🚀 Features

* 🎴 Randomised card dealing system
* 🤖 Automated dealer logic (draws until reaching 17)
* ♠️ Ace handling (dynamically adjusts between 11 and 1 to prevent busting)
* 🔁 Continuous gameplay loop with user decision-making
* ⚖️ Win, lose, and draw outcome handling

---

## 🧠 Key Concepts Demonstrated

* **State management** across multiple entities (player vs dealer)
* **Modular programming** using well-structured functions
* **Game logic implementation** based on real-world rules
* **Edge case handling** (e.g. Ace value adjustment to avoid busting)
* **Control flow design** for interactive CLI applications

---

## 🛠 Tech Stack

* Python 3

---

## ▶️ How to Run

1. Clone the repository:

```id="t7u4ck"
git clone https://github.com/your-username/python-projects-portfolio.git
```

2. Navigate to the project folder:

```id="a6o0jq"
cd games/blackjack-game-python
```

3. Run the program:

```id="h8g2d9"
python main.py
```

---

## 📂 Project Structure

```id="r5wq1x"
blackjack-game-python/
├── main.py     # Core game logic and flow
├── art.py      # ASCII art / game visuals
└── README.md
```

---

## 🔍 Design Notes

The game separates responsibilities into distinct functions (e.g. dealing cards, handling turns, computing outcomes), making the logic easier to follow and extend.

Special attention is given to handling Aces dynamically, ensuring gameplay remains accurate to Blackjack rules.

---

## 🎯 Key Takeaway

This project demonstrates the ability to design and implement a rule-based interactive system with multiple components, highlighting strong foundations in problem-solving and program structure.
