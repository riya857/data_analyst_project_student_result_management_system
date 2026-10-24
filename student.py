from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
db_name="srms.db"
def get_db_connection():
    return sqlite3.connect(db_name)

class StudentClass:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1100x600+150+80")
        self.root.config(bg="white")

        # ================= TITLE =================

        title = Label(
            self.root,
            text="Student Management System",
            font=("times new roman", 25, "bold"),
            bg="#0B4F9C",
            fg="white"
        )
        title.place(x=0, y=0, width=1100, height=50)

        # ================= LEFT FRAME =================

        left = Frame(
            self.root,
            bd=2,
            relief=RIDGE,
            bg="white"
        )
        left.place(x=10, y=60, width=430, height=525)

        Label(
            left,
            text="Student Details",
            font=("times new roman", 18, "bold"),
            bg="#0B4F9C",
            fg="white"
        ).place(x=0, y=0, width=426, height=40)

        # Variables

        self.roll = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.dob = StringVar()
        self.contact = StringVar()
        self.course = StringVar()
        self.admission = StringVar()

        # Roll

        Label(
            left,
            text="Roll No.",
            font=("times new roman", 15),
            bg="white"
        ).place(x=20, y=60)

        Entry(
            left,
            textvariable=self.roll,
            font=("times new roman", 14)
        ).place(x=140, y=60, width=250, height=30)

        # Name

        Label(
            left,
            text="Name",
            font=("times new roman", 15),
            bg="white"
        ).place(x=20, y=105)

        Entry(
            left,
            textvariable=self.name,
            font=("times new roman", 14)
        ).place(x=140, y=105, width=250, height=30)

        # Email

        Label(
            left,
            text="Email",
            font=("times new roman", 15),
            bg="white"
        ).place(x=20, y=150)

        Entry(
            left,
            textvariable=self.email,
            font=("times new roman", 14)
        ).place(x=140, y=150, width=250, height=30)

        # Gender

        Label(
            left,
            text="Gender",
            font=("times new roman", 15),
            bg="white"
        ).place(x=20, y=195)

        ttk.Combobox(
            left,
            textvariable=self.gender,
            values=("Male", "Female", "Other"),
            state="readonly",
            font=("times new roman", 13)
        ).place(x=140, y=195, width=250, height=30)

        # DOB

        Label(
            left,
            text="D.O.B",
            font=("times new roman", 15),
            bg="white"
        ).place(x=20, y=240)

        Entry(
            left,
            textvariable=self.dob,
            font=("times new roman", 14)
        ).place(x=140, y=240, width=250, height=30)

        # Contact

        Label(
            left,
            text="Contact",
            font=("times new roman", 15),
            bg="white"
        ).place(x=20, y=285)

        Entry(
            left,
            textvariable=self.contact,
            font=("times new roman", 14)
        ).place(x=140, y=285, width=250, height=30)

        # Course

        Label(
            left,
            text="Course",
            font=("times new roman", 15),
            bg="white"
        ).place(x=20, y=330)

        Entry(
            left,
            textvariable=self.course,
            font=("times new roman", 14)
        ).place(x=140, y=330, width=250, height=30)

        # Admission

        Label(
            left,
            text="Admission",
            font=("times new roman", 15),
            bg="white"
        ).place(x=20, y=375)

        Entry(
            left,
            textvariable=self.admission,
            font=("times new roman", 14)
        ).place(x=140, y=375, width=250, height=30)

        # Buttons

        Button(
            left,
            text="Save",
            command=self.save,
            bg="green",
            fg="white",
            font=("times new roman", 12, "bold")
        ).place(x=20, y=430, width=90, height=35)

        Button(
            left,
            text="Update",
            command=self.update,
            bg="blue",
            fg="white",
            font=("times new roman", 12, "bold")
        ).place(x=120, y=430, width=90, height=35)

        Button(
            left,
            text="Delete",
            command=self.delete,
            bg="red",
            fg="white",
            font=("times new roman", 12, "bold")
        ).place(x=220, y=430, width=90, height=35)

        Button(
            left,
            text="Clear",
            command=self.clear,
            bg="gray",
            fg="white",
            font=("times new roman", 12, "bold")
        ).place(x=320, y=430, width=90, height=35)

        # ================= RIGHT FRAME =================

        right = Frame(
            self.root,
            bd=2,
            relief=RIDGE,
            bg="white"
        )
        right.place(x=450, y=60, width=640, height=525)

        Label(
            right,
            text="Student List",
            font=("times new roman", 18, "bold"),
            bg="#0B4F9C",
            fg="white"
        ).place(x=0, y=0, width=636, height=40)

        # Table

        table_frame = Frame(right, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=50, width=625, height=450)

        scroll_x = Scrollbar(
            table_frame,
            orient=HORIZONTAL
        )
        scroll_y = Scrollbar(
            table_frame,
            orient=VERTICAL
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=(
                "roll",
                "name",
                "email",
                "gender",
                "dob",
                "contact",
                "course",
                "admission"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        self.table.heading("roll", text="Roll No.")
        self.table.heading("name", text="Name")
        self.table.heading("email", text="Email")
        self.table.heading("gender", text="Gender")
        self.table.heading("dob", text="D.O.B")
        self.table.heading("contact", text="Contact")
        self.table.heading("course", text="Course")
        self.table.heading("admission", text="Admission")

        self.table["show"] = "headings"

        self.table.column("roll", width=80)
        self.table.column("name", width=120)
        self.table.column("email", width=180)
        self.table.column("gender", width=80)
        self.table.column("dob", width=100)
        self.table.column("contact", width=100)
        self.table.column("course", width=100)
        self.table.column("admission", width=100)

        self.table.pack(fill=BOTH, expand=1)

    # ================= SAVE =================

    def save(self):

        messagebox.showinfo(
            "Student",
            "Save button working hai."
        )

    # ================= UPDATE =================

    def update(self):

        messagebox.showinfo(
            "Student",
            "Update button working hai."
        )

    # ================= DELETE =================

    def delete(self):

        messagebox.showinfo(
            "Student",
            "Delete button working hai."
        )

    # ================= CLEAR =================

    def clear(self):

        self.roll.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.dob.set("")
        self.contact.set("")
        self.course.set("")
        self.admission.set("")


# ================= RUN =================

if __name__ == "__main__":

    root = Tk()

    obj = StudentClass(root)

    root.mainloop()