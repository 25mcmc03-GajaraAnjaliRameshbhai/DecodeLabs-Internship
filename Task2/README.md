# Expense Tracker

## Description

Expense Tracker is a command-line Python application developed as part of the DecodeLabs Python Programming Internship.

The program allows users to continuously enter expense amounts and keeps track of the total amount spent. When the user enters `quit`, the program displays a complete expense summary.

## Features

- Add multiple expense amounts
- Display the running total
- Store entered expenses
- Calculate total spending
- Calculate average spending
- Display the highest expense
- Display the lowest expense
- Display all entered expenses
- Reject negative expenses
- Handle invalid input using exception handling
- Exit by entering `quit`

## Technologies Used

- Python 3

## Concepts Used

- Python Lists
- `while` loops
- Accumulator pattern
- `try-except` exception handling
- Type conversion using `float()`
- Conditional statements
- `max()` and `min()`
- `enumerate()`
- User input and validation

## How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python expense_tracker.py
```

> If your Python file has a different name, replace `expense_tracker.py` with the actual filename.

## Example

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

Enter expense amount: quit

========================================
        EXPENSE SUMMARY
========================================
Total Expenses : 2
Total Spent    : ₹150.00
Average Spend  : ₹75.00
Highest Spend  : ₹100.00
Lowest Spend   : ₹50.00

Expense List
1. ₹100.00
2. ₹50.00

Thank you!
```

## Project Information

**Project:** Project 2 - Expense Tracker  
**Domain:** Python Programming  
**Internship:** DecodeLabs  
**Batch:** 2026
