# Import required libraries
import oracledb              # For connecting to Oracle database
import matplotlib.pyplot as plt   # For creating graphs

# Initialize Oracle client with the local path
oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\instantclient_21_17")

try:
    # Connect to the Oracle database
    connection = oracledb.connect(
        user="hr",            # Username for the database
        password="hr",        # Password for the database
        dsn="localhost/XE"    # Data Source Name (XE = Oracle Express Edition)
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # ===== MENU SECTION =====
    print("=== Student Graph Generator ===")
    print("1. Show graphs for all students")
    print("2. Show graph for a specific student by ID")
    print("3. Show graphs for students of a specific standard")

    # Get user choice
    choice = input("Enter your choice (1, 2 or 3): ")

    # If user selects option 1, fetch all students
    if choice == '1':
        cursor.execute("SELECT STUDENT_ID, STUDENT_NAME, PHYSICS, CHEMISTRY, MATH, STANDARD, REMARK FROM students")
        rows = cursor.fetchall()

    # If user selects option 2, fetch student by ID
    elif choice == '2':
        student_id_input = input("Enter Student ID: ")
        cursor.execute("""
            SELECT STUDENT_ID, STUDENT_NAME, PHYSICS, CHEMISTRY, MATH, STANDARD, REMARK 
            FROM students 
            WHERE STUDENT_ID = :id
        """, {'id': student_id_input})
        rows = cursor.fetchall()

        # If no student is found, show message
        if not rows:
            print(" No student found with that ID.")
            rows = []

    # If user selects option 3, fetch students by standard
    elif choice == '3':
        standard_input = input("Enter Standard: ")
        cursor.execute("""
            SELECT STUDENT_ID, STUDENT_NAME, PHYSICS, CHEMISTRY, MATH, STANDARD, REMARK 
            FROM students 
            WHERE STANDARD = :std
        """, {'std': standard_input})
        rows = cursor.fetchall()

        # If no students are found, show message
        if not rows:
            print(" No students found for that standard.")
            rows = []

    # If user enters an invalid choice
    else:
        print(" Invalid choice.")
        rows = []

    # ===== GRAPH GENERATION SECTION =====
    # Generate graph for each student
    for row in rows:
        student_id, name, physics, chemistry, math, standard, remark = row

        # List of subjects
        subjects = ['Physics', 'Chemistry', 'Math']

        # If marks are None, replace with 0
        scores = [s if s is not None else 0 for s in [physics, chemistry, math]]

        # Create a bar graph
        plt.figure(figsize=(6, 4))  # Set graph size
        plt.bar(subjects, scores, color=['blue', 'green', 'orange'])  # Create bars
        plt.title(f"ID: {student_id} | {name}\nStandard: {standard} | Remark: {remark}")  # Graph title
        plt.ylim(0, 100)  # Y-axis limit
        plt.ylabel("Marks")  # Y-axis label
        plt.xlabel("Subjects")  # X-axis label
        plt.tight_layout()  # Adjust layout
        plt.show()  # Show the graph

    # If data was found, show success message
    if rows:
        print("✅ Graph(s) displayed successfully!")

# If any error occurs, print it
except Exception as e:
    print(" Error:", e)

# Always close the connection to the database
finally:
    if connection:
        connection.close()
