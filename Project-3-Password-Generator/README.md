# 🔐 Random Password Generator

## 📌 Description

The **Random Password Generator** is a command-line Python application developed as Project 3 of my **DecodeLabs Python Programming Internship**.

The program generates a secure random password based on the length entered by the user. It ensures that every generated password contains uppercase letters, lowercase letters, digits, and special characters.

The project demonstrates the use of Python's built-in modules, string manipulation, functions, input validation, and secure random character generation.

---

## ✨ Features

- Generate secure random passwords
- User-defined password length
- Minimum password length of 8 characters
- Maximum password length of 64 characters
- Guarantees at least one uppercase letter (`A-Z`)
- Guarantees at least one lowercase letter (`a-z`)
- Guarantees at least one digit (`0-9`)
- Guarantees at least one special character
- Securely shuffles password characters
- Validates the generated password
- Handles invalid user input

---

## 🔒 Password Requirements

Every generated password contains:

- ✅ At least one uppercase letter
- ✅ At least one lowercase letter
- ✅ At least one digit
- ✅ At least one special character
- ✅ Minimum length: 8 characters
- ✅ Maximum length: 64 characters

---

## 🛠️ Technologies Used

- Python 3
- `secrets` module
- `string` module

No external Python packages are required.

---

## 📚 Concepts Used

- Python Functions
- String Manipulation
- Built-in Python Modules
- `secrets.choice()`
- `string.ascii_uppercase`
- `string.ascii_lowercase`
- `string.digits`
- `string.punctuation`
- Lists
- Loops
- Conditional Statements
- Exception Handling
- Input Validation
- `any()`
- `join()`

---

## ▶️ How to Run

1. Make sure **Python 3** is installed on your system.

2. Open a terminal in the project folder.

3. Run:

```bash
python password_generator.py
```

4. Enter the required password length when prompted.

---

## 💻 Example Output

```text
==================================================
          RANDOM PASSWORD GENERATOR
==================================================

Password Requirements:
• Minimum 8 characters
• At least one uppercase letter (A-Z)
• At least one lowercase letter (a-z)
• At least one digit (0-9)
• At least one special character (!, @, #, $, etc.)

Enter password length (8-64): 12

==================================================
Generated Password:
p7@Jm!4qZ2#x
==================================================

Password Validation:
✓ Uppercase letter included
✓ Lowercase letter included
✓ Digit included
✓ Special character included
✓ Password length: 12

Password generated successfully!
```

> The generated password will be different each time the program runs.

---

## ⚙️ How It Works

1. The user enters the desired password length.
2. The program validates that the length is between 8 and 64.
3. One character is selected from each required category:
   - Uppercase letter
   - Lowercase letter
   - Digit
   - Special character
4. The remaining characters are generated securely using the `secrets` module.
5. All characters are shuffled.
6. The program validates that all password requirements are satisfied.
7. The final password is displayed to the user.

---

## 📂 Project Structure

```text
Project-3-Password-Generator/
│
├── password_generator.py
└── README.md
```

---

## 🎯 Learning Outcomes

Through this project, I practised:

- Working with Python built-in modules
- Generating secure random values
- String manipulation
- Creating reusable functions
- Input and exception handling
- Password validation
- Working with lists and loops
- Writing structured and readable Python programs

---

## 👩‍💻 Project Information

**Project:** Project 3 - Random Password Generator  
**Domain:** Python Programming  
**Organization:** DecodeLabs  
**Batch:** 2026  

---

*Developed as part of the DecodeLabs Python Programming Internship.*
