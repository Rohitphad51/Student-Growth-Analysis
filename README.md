# 📊 Student Growth Visualizer using Oracle DB & Python

This project is a command-line Python tool to **analyze and visualize student academic performance** using an Oracle database backend. It allows users to generate subject-wise bar graphs for students based on user inputs like Student ID or Class Standard. It’s built for schools or institutions that want to visualize performance data from a central database.

---

## 🎯 Project Objectives

- Connect to Oracle database and fetch student data.
- Generate **bar graphs** for subjects (Physics, Chemistry, Math).
- Provide 3 different modes for graphing:
  - All students
  - Specific student by ID
  - All students from a specific standard

---

## 🧾 Dataset Structure (Oracle Table)

Expected table name: `students`

| Column Name     | Type     | Description                         |
|-----------------|----------|-------------------------------------|
| STUDENT_ID      | Number   | Unique ID for student               |
| STUDENT_NAME    | Varchar  | Name of the student                 |
| PHYSICS         | Number   | Physics marks (0-100)               |
| CHEMISTRY       | Number   | Chemistry marks (0-100)             |
| MATH            | Number   | Math marks (0-100)                  |
| STANDARD        | Varchar  | Class/Grade                         |
| REMARK          | Varchar  | Remarks (Pass/Fail/Excellent etc.)  |

---

## 🚀 Features

- 📦 Connects to **Oracle XE (Express Edition)** database
- 📊 Generates subject-wise **bar charts** for each student
- 🔎 Fetches student info by ID or by standard
- 💥 Handles missing data gracefully
- 🧼 CLI-based user interaction
- ✅ Clean code with error handling

---

## 🛠 Requirements

- Python 3.7+
- Oracle XE Database
- Instant Client for Oracle installed locally
- Python packages:
  - `oracledb`
  - `matplotlib`

---

## 🔧 Installation & Setup

### 🔹 1. Install Oracle Client

Download and extract the Oracle Instant Client from:  
👉 https://www.oracle.com/database/technologies/instant-client.html

Update path in script:
```python
oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\instantclient_21_17")
