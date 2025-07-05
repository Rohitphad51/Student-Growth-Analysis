# 🎓 Student Growth Visualizer

A Python project that connects to an Oracle database and generates subject-wise performance graphs for students. It allows you to visualize marks in Physics, Chemistry, and Math with clean bar graphs using `matplotlib`.

---

## 📖 Project Overview

This is a simple CLI-based educational data visualization tool that helps teachers or institutions to:

- View and analyze student marks.
- Generate bar graphs for each student.
- Filter data by student ID or standard.

All data is fetched from an Oracle database in real time.

---

## 🚀 Features

- 📊 Graphs for all students in the database.
- 🔍 Filter by **Student ID** to view individual performance.
- 🏫 Filter by **Standard** (class) to see students of a particular grade.
- 🎨 Beautiful bar graphs showing marks in Physics, Chemistry, and Math.
- ⚠️ Handles missing values (None) by treating them as 0.

---

## 🧰 Technologies Used

| Component     | Technology            |
|---------------|------------------------|
| Programming   | Python 3.x             |
| Database      | Oracle XE              |
| DB Connector  | `oracledb` (Python)    |
| Graph Plotting| `matplotlib`           |

---

## 🗃️ Database Schema (Table: `students`)

Ensure your Oracle database contains a table named `students` with the following structure:

```sql
CREATE TABLE students (
     Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 STUDENT_ID                                NOT NULL NUMBER
 STUDENT_NAME                                       VARCHAR2(30)
 PHYSICS                                            NUMBER
 CHEMISTRY                                          NUMBER
 MATH                                               NUMBER
 STANDARD                                           VARCHAR2(10)
 REMARK                                             VARCHAR2(20)

);
