import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# =========================================================
# DATABASE
# =========================================================

DB_NAME = "srms.db"


def get_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    con = get_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            duration TEXT,
            charges TEXT,
            description TEXT
        )
    """)

    con.commit()
    con.close()


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()
root.title("Student Result Management System")
root.geometry("1200x700")
root.configure(bg="white")

selected_id = None


# =========================================================
# TITLE
# =========================================================

title = tk.Label(
    root,
    text="Manage Course Details",
    font=("Arial", 24, "bold"),
    bg="#0B4F9C",
    fg="white",
    pady=15
)

title.pack(fill="x")


# =========================================================
# MAIN FRAME
# =========================================================

main = tk.Frame(
    root,
    bg="white"
)

main.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=20
)


# =========================================================
# LEFT FRAME
# =========================================================

left = tk.Frame(
    main,
    bg="white"
)

left.pack(
    side="left",
    fill="y",
    padx=(0, 30)
)


# =========================================================
# RIGHT FRAME
# =========================================================

right = tk.Frame(
    main,
    bg="white"
)

right.pack(
    side="right",
    fill="both",
    expand=True
)


# =========================================================
# COURSE NAME
# =========================================================

tk.Label(
    left,
    text="Course Name",
    font=("Arial", 14, "bold"),
    bg="white"
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=12
)


course_name = tk.Entry(
    left,
    width=30,
    font=("Arial", 14),
    bg="white",
    fg="black"
)

course_name.grid(
    row=0,
    column=1,
    padx=15,
    pady=12
)


# =========================================================
# DURATION
# =========================================================

tk.Label(
    left,
    text="Duration",
    font=("Arial", 14, "bold"),
    bg="white"
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=12
)


duration = tk.Entry(
    left,
    width=30,
    font=("Arial", 14),
    bg="white",
    fg="black"
)

duration.grid(
    row=1,
    column=1,
    padx=15,
    pady=12
)


# =========================================================
# CHARGES
# =========================================================

tk.Label(
    left,
    text="Charges",
    font=("Arial", 14, "bold"),
    bg="white"
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=12
)


charges = tk.Entry(
    left,
    width=30,
    font=("Arial", 14),
    bg="white",
    fg="black"
)

charges.grid(
    row=2,
    column=1,
    padx=15,
    pady=12
)


# =========================================================
# DESCRIPTION
# =========================================================

tk.Label(
    left,
    text="Description",
    font=("Arial", 14, "bold"),
    bg="white"
).grid(
    row=3,
    column=0,
    sticky="nw",
    pady=12
)


description = tk.Text(
    left,
    width=30,
    height=8,
    font=("Arial", 13),
    bg="white",
    fg="black"
)

description.grid(
    row=3,
    column=1,
    padx=15,
    pady=12
)


# =========================================================
# LOAD COURSES
# =========================================================

def load_courses():

    global selected_id

    selected_id = None

    # Table clear
    for item in table.get_children():
        table.delete(item)

    try:

        con = get_db()
        cur = con.cursor()

        cur.execute("""
            SELECT
                course_id,
                course_name,
                duration,
                charges
            FROM course
            ORDER BY course_id ASC
        """)

        rows = cur.fetchall()

        # Serial number
        serial_no = 1

        for row in rows:

            actual_id = row[0]

            table.insert(
                "",
                tk.END,
                iid=str(actual_id),
                values=(
                    serial_no,
                    row[1],
                    row[2],
                    row[3]
                )
            )

            serial_no += 1

        cur.close()
        con.close()

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================================================
# CLEAR
# =========================================================

def clear_fields():

    global selected_id

    selected_id = None

    # Course Name clear
    course_name.delete(
        0,
        tk.END
    )

    # Duration clear
    duration.delete(
        0,
        tk.END
    )

    # Charges clear
    charges.delete(
        0,
        tk.END
    )

    # Description clear
    description.delete(
        "1.0",
        tk.END
    )

    # Search clear
    search_entry.delete(
        0,
        tk.END
    )

    # Selection remove
    for item in table.selection():
        table.selection_remove(item)

    course_name.focus_set()


# =========================================================
# SAVE COURSE
# =========================================================

def save_course():

    name = course_name.get().strip()

    if name == "":

        messagebox.showwarning(
            "Warning",
            "Please enter Course Name."
        )

        course_name.focus_set()

        return

    try:

        con = get_db()
        cur = con.cursor()

        # Check duplicate course
        cur.execute(
            """
            SELECT course_id
            FROM course
            WHERE course_name = ?
            """,
            (name,)
        )

        existing = cur.fetchone()

        if existing is not None:

            messagebox.showwarning(
                "Warning",
                "Course Name already exists."
            )

            cur.close()
            con.close()

            return

        # Insert course
        cur.execute(
            """
            INSERT INTO course
            (
                course_name,
                duration,
                charges,
                description
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                name,
                duration.get().strip(),
                charges.get().strip(),
                description.get(
                    "1.0",
                    tk.END
                ).strip()
            )
        )

        con.commit()

        cur.close()
        con.close()

        messagebox.showinfo(
            "Success",
            "Course saved successfully."
        )

        clear_fields()
        load_courses()

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================================================
# SELECT COURSE
# =========================================================

def select_course(event=None):

    global selected_id

    selected = table.selection()

    if not selected:
        return

    # IMPORTANT:
    # iid = actual database course_id
    selected_id = int(selected[0])

    try:

        con = get_db()
        cur = con.cursor()

        cur.execute(
            """
            SELECT
                course_name,
                duration,
                charges,
                description
            FROM course
            WHERE course_id = ?
            """,
            (selected_id,)
        )

        row = cur.fetchone()

        cur.close()
        con.close()

        if row is None:
            return

        # Course Name
        course_name.delete(
            0,
            tk.END
        )

        course_name.insert(
            0,
            row[0] or ""
        )

        # Duration
        duration.delete(
            0,
            tk.END
        )

        duration.insert(
            0,
            row[1] or ""
        )

        # Charges
        charges.delete(
            0,
            tk.END
        )

        charges.insert(
            0,
            row[2] or ""
        )

        # Description
        description.delete(
            "1.0",
            tk.END
        )

        description.insert(
            "1.0",
            row[3] or ""
        )

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================================================
# UPDATE COURSE
# =========================================================

def update_course():

    global selected_id

    if selected_id is None:

        messagebox.showwarning(
            "Warning",
            "Please select a course from the table."
        )

        return

    name = course_name.get().strip()

    if name == "":

        messagebox.showwarning(
            "Warning",
            "Course Name is required."
        )

        course_name.focus_set()

        return

    try:

        con = get_db()
        cur = con.cursor()

        # Check duplicate except current course
        cur.execute(
            """
            SELECT course_id
            FROM course
            WHERE course_name = ?
            AND course_id != ?
            """,
            (
                name,
                selected_id
            )
        )

        existing = cur.fetchone()

        if existing is not None:

            messagebox.showwarning(
                "Warning",
                "Another course with this name already exists."
            )

            cur.close()
            con.close()

            return

        cur.execute(
            """
            UPDATE course
            SET
                course_name = ?,
                duration = ?,
                charges = ?,
                description = ?
            WHERE course_id = ?
            """,
            (
                name,
                duration.get().strip(),
                charges.get().strip(),
                description.get(
                    "1.0",
                    tk.END
                ).strip(),
                selected_id
            )
        )

        con.commit()

        cur.close()
        con.close()

        messagebox.showinfo(
            "Success",
            "Course updated successfully."
        )

        clear_fields()
        load_courses()

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================================================
# DELETE COURSE
# =========================================================

def delete_course():

    global selected_id

    if selected_id is None:

        messagebox.showwarning(
            "Warning",
            "Please select a course from the table."
        )

        return

    # Confirmation
    answer = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this course?"
    )

    if answer is False:
        return

    try:

        con = get_db()
        cur = con.cursor()

        cur.execute(
            """
            DELETE FROM course
            WHERE course_id = ?
            """,
            (selected_id,)
        )

        con.commit()

        deleted_rows = cur.rowcount

        cur.close()
        con.close()

        if deleted_rows > 0:

            messagebox.showinfo(
                "Success",
                "Course deleted successfully."
            )

        else:

            messagebox.showwarning(
                "Warning",
                "Course not found."
            )

        clear_fields()
        load_courses()

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================================================
# SEARCH COURSE
# =========================================================

def search_course():

    global selected_id

    selected_id = None

    text = search_entry.get().strip()

    # Table clear
    for item in table.get_children():
        table.delete(item)

    try:

        con = get_db()
        cur = con.cursor()

        if text == "":

            cur.execute(
                """
                SELECT
                    course_id,
                    course_name,
                    duration,
                    charges
                FROM course
                ORDER BY course_id ASC
                """
            )

        else:

            cur.execute(
                """
                SELECT
                    course_id,
                    course_name,
                    duration,
                    charges
                FROM course
                WHERE course_name LIKE ?
                ORDER BY course_id ASC
                """,
                (
                    "%" + text + "%",
                )
            )

        rows = cur.fetchall()

        # Search result serial number
        serial_no = 1

        for row in rows:

            actual_id = row[0]

            table.insert(
                "",
                tk.END,
                iid=str(actual_id),
                values=(
                    serial_no,
                    row[1],
                    row[2],
                    row[3]
                )
            )

            serial_no += 1

        cur.close()
        con.close()

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================================================
# BUTTON FRAME
# =========================================================

button_frame = tk.Frame(
    left,
    bg="white"
)

button_frame.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=20
)


# =========================================================
# SAVE BUTTON
# =========================================================

save_button = tk.Button(
    button_frame,
    text="Save",
    width=10,
    font=("Arial", 12, "bold"),
    bg="#1597D4",
    fg="white",
    cursor="hand2",
    command=save_course
)

save_button.grid(
    row=0,
    column=0,
    padx=4
)


# =========================================================
# UPDATE BUTTON
# =========================================================

update_button = tk.Button(
    button_frame,
    text="Update",
    width=10,
    font=("Arial", 12, "bold"),
    bg="#38A169",
    fg="white",
    cursor="hand2",
    command=update_course
)

update_button.grid(
    row=0,
    column=1,
    padx=4
)


# =========================================================
# DELETE BUTTON
# =========================================================

delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=10,
    font=("Arial", 12, "bold"),
    bg="#D53F8C",
    fg="white",
    cursor="hand2",
    command=delete_course
)

delete_button.grid(
    row=0,
    column=2,
    padx=4
)


# =========================================================
# CLEAR BUTTON
# =========================================================

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=10,
    font=("Arial", 12, "bold"),
    bg="#6675A6",
    fg="white",
    cursor="hand2",
    command=clear_fields
)

clear_button.grid(
    row=0,
    column=3,
    padx=4
)


# =========================================================
# SEARCH FRAME
# =========================================================

search_frame = tk.Frame(
    right,
    bg="white"
)

search_frame.pack(
    fill="x",
    pady=(0, 12)
)


# =========================================================
# SEARCH LABEL
# =========================================================

tk.Label(
    search_frame,
    text="Search Course:",
    font=("Arial", 13, "bold"),
    bg="white"
).pack(
    side="left"
)


# =========================================================
# SEARCH ENTRY
# =========================================================

search_entry = tk.Entry(
    search_frame,
    width=25,
    font=("Arial", 13),
    bg="white",
    fg="black"
)

search_entry.pack(
    side="left",
    padx=10
)


# =========================================================
# SEARCH BUTTON
# =========================================================

search_button = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 11, "bold"),
    bg="#0B4F9C",
    fg="white",
    cursor="hand2",
    command=search_course
)

search_button.pack(
    side="left",
    padx=5
)


# =========================================================
# SHOW ALL BUTTON
# =========================================================

show_all_button = tk.Button(
    search_frame,
    text="Show All",
    font=("Arial", 11, "bold"),
    bg="#555555",
    fg="white",
    cursor="hand2",
    command=load_courses
)

show_all_button.pack(
    side="left",
    padx=5
)


# =========================================================
# TABLE FRAME
# =========================================================

table_frame = tk.Frame(
    right,
    bg="white"
)

table_frame.pack(
    fill="both",
    expand=True
)


# =========================================================
# SCROLLBAR
# =========================================================

scroll_y = ttk.Scrollbar(
    table_frame,
    orient="vertical"
)

scroll_y.pack(
    side="right",
    fill="y"
)


# =========================================================
# TABLE
# =========================================================

table = ttk.Treeview(
    table_frame,
    columns=(
        "id",
        "name",
        "duration",
        "charges"
    ),
    show="headings",
    yscrollcommand=scroll_y.set
)


scroll_y.config(
    command=table.yview
)


# =========================================================
# TABLE HEADINGS
# =========================================================

table.heading(
    "id",
    text="Course ID"
)

table.heading(
    "name",
    text="Course Name"
)

table.heading(
    "duration",
    text="Duration"
)

table.heading(
    "charges",
    text="Charges"
)


# =========================================================
# TABLE COLUMNS
# =========================================================

table.column(
    "id",
    width=100,
    anchor="center"
)

table.column(
    "name",
    width=220,
    anchor="center"
)

table.column(
    "duration",
    width=160,
    anchor="center"
)

table.column(
    "charges",
    width=140,
    anchor="center"
)


table.pack(
    fill="both",
    expand=True
)


# =========================================================
# TABLE CLICK
# =========================================================

table.bind(
    "<<TreeviewSelect>>",
    select_course
)


# =========================================================
# ENTER KEY SEARCH
# =========================================================

search_entry.bind(
    "<Return>",
    lambda event: search_course()
)


# =========================================================
# START PROGRAM
# =========================================================

create_table()

load_courses()

course_name.focus_set()

root.mainloop()
if __name__ == "__main__":
    create_table()
    print("Database and table created successfully.")