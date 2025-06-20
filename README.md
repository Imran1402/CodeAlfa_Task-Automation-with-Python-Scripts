# CodeAlpha_Task_Automation_with_Python_Scripts

## ✅ Task 3: Task Automation - Email Extraction Script

This project is part of the CodeAlpha Python Internship. The goal of this task is to **automate a real-life repetitive task** using Python.  
For this task, I created a script that **extracts all email addresses** from a `.txt` file and saves them to a new file.

---

## 🔧 Features

- Scans any given `.txt` file for valid email addresses.
- Uses regular expressions to detect and extract emails.
- Eliminates duplicate emails.
- Saves the clean list of emails to an output `.txt` file.

---

## 🧠 Key Concepts Used

- `re` module (Regular Expressions)
- File handling (`open`, `read`, `write`)
- Sets for removing duplicates
- Basic error handling with `try-except`

---

## 📁 File Structure

```bash
.
├── sample_input.txt              # Input file containing raw text with email addresses
├── extracted_emails.txt          # Output file containing extracted email addresses
├── CodeAlpha_Task_Automation_with_Python_Scripts.py   # Main Python script
└── README.md
