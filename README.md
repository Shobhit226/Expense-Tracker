# Personal Expense Tracker

This is a command-line based Python program for recording and reviewing daily personal expenses.

## Features

- Add an expense with date, category, amount, and a note.
- View all recorded expenses.
- View total spending and spending summary by category.
- Automatically saves and loads data from a file.

## How It Works

1. When the program starts, it loads previously saved expenses from a CSV file.
2. The user is shown a menu with options to:
   - Add a new expense
   - View all recorded expenses
   - View a total and category-wise summary
   - Exit the program
3. When adding an expense, the user is prompted to enter the date, category, amount, and an optional note.
4. All expenses are saved in a file named `expenses.csv` so they remain available the next time the program is run.

## File Information

- `Expense-Tracker.py` – The main Python script.
- `expenses.csv` – The file where all expenses are saved. This file is created automatically if it does not exist.

## Requirements

- Python 3.x
- No external libraries are required.

## How to Run

From a terminal or command prompt, run the following:

```bash
python expense_tracker.py
