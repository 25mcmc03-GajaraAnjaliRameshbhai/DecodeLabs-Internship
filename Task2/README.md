# 💰 Expense Tracker

## 📌 Description

The Expense Tracker is a command-line application developed using Python as part of the DecodeLabs Python Programming Internship.

The program allows users to continuously enter their expense amounts and keeps track of the running total. When the user enters `quit`, the application displays a summary containing the total number of expenses, total amount spent, average expense, highest expense, lowest expense, and a list of all entered expenses.

## ✨ Features

- Add multiple expense amounts
- Display the running total after every entry
- Store all entered expenses
- Calculate total spending
- Calculate average spending
- Display the highest expense
- Display the lowest expense
- Display a numbered list of expenses
- Reject negative expense amounts
- Handle invalid input using exception handling
- Exit the program using the `quit` command

## 🛠️ Technologies Used

- Python 3

## 📚 Concepts Used

- Python Lists
- `while` loop
- `try-except` exception handling
- `float()` type conversion
- Conditional statements
- Accumulator pattern
- `len()`
- `max()`
- `min()`
- `enumerate()`
- User input and validation

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python installation using:

```bash
python --version
```

### 2. Open the project folder in a terminal

Navigate to the folder containing `expense_tracker.py`.

### 3. Run the program

```bash
python expense_tracker.py
```

### 4. Enter expenses

Enter expense amounts one at a time.

Type:

```text
quit
```

when you want to stop entering expenses and view the final summary.

## 💻 Example Output

```text
========================================
        EXPENSE TRACKER
========================================
Type 'quit' anytime to finish.

Enter expense amount: 100
Added ₹100.00
Running Total: ₹100.00

Enter expense amount: 50
Added ₹50.00
Running Total: ₹150.00

Enter expense amount: 25
Added ₹25.00
Running Total: ₹175.00

Enter expense amount: quit

========================================
        EXPENSE SUMMARY
========================================
Total Expenses : 3
Total Spent    : ₹175.00
Average Spend  : ₹58.33
Highest Spend  : ₹100.00
Lowest Spend   : ₹25.00

Expense List
1. ₹100.00
2. ₹50.00
3. ₹25.00

Thank you!
```

## 📂 Project Structure

```text
Project-2-Expense-Tracker/
│
├── expense_tracker.py
└── README.md
```

## 🎯 Learning Outcome

Through this project, I practiced continuous user input, Python lists, loops, exception handling, input validation, accumulator logic, and basic calculations on stored data.

## 👩‍💻 Project Information

**Project:** Project 2 - Expense Tracker  
**Domain:** Python Programming  
**Internship:** DecodeLabs  
**Year:** 2026
