from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class ViewResultClass:

    def __init__(self, root):

        self.root = root
        self.root.title("View Student Result")
        self.root.geometry("1100x600+150+80")
        self.root.config(bg="white")
        self.root.focus_force()

        # ================= VARIABLES =================

        self.var_roll = StringVar()

        # ================= TITLE =================

        title = Label(
            self.root,
            text="View Student Result",
            font=("times new roman", 25, "bold"),
            bg="#0B4F9C",
            fg="white"
        )
        title.pack(side=TOP, fill=X)

        # ================= SEARCH FRAME =================

        search_frame = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        search_frame.place(
            x=10,
            y=70,
            width=1080,
            height=80
        )

        Label(
            search_frame,
            text="Enter Roll No.",
            font=("times new roman", 16, "bold"),
            bg="white"
        ).place(
            x=20,
            y=22
        )

        Entry(
            search_frame,
            textvariable=self.var_roll,
            font=("times new roman", 16),
            bg="lightyellow"
        ).place(
            x=180,
            y=20,
            width=250,
            height=35
        )

        # ================= SEARCH BUTTON =================

        Button(
            search_frame,
            text="Search",
            command=self.search,
            font=("times new roman", 13, "bold"),
            bg="#0B4F9C",
            fg="white",
            cursor="hand2"
        ).place(
            x=450,
            y=20,
            width=100,
            height=35
        )

        # ================= SHOW ALL BUTTON =================

        Button(
            search_frame,
            text="Show All",
            command=self.show_all,
            font=("times new roman", 13, "bold"),
            bg="green",
            fg="white",
            cursor="hand2"
        ).place(
            x=570,
            y=20,
            width=100,
            height=35
        )

        # ================= RESULT TABLE =================

        table_frame = Frame(
            self.root,
            bd=2,
            relief=RIDGE,
            bg="white"
        )

        table_frame.place(
            x=10,
            y=170,
            width=1080,
            height=380
        )

        # ================= SCROLLBARS =================

        scroll_y = Scrollbar(
            table_frame,
            orient=VERTICAL
        )

        scroll_x = Scrollbar(
            table_frame,
            orient=HORIZONTAL
        )

        # ================= TREEVIEW =================

        self.result_table = ttk.Treeview(
            table_frame,
            columns=(
                "roll",
                "name",
                "course",
                "subject",
                "marks",
                "full_marks"
            ),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
            show="headings"
        )

        scroll_y.pack(
            side=RIGHT,
            fill=Y
        )

        scroll_x.pack(
            side=BOTTOM,
            fill=X
        )

        scroll_y.config(
            command=self.result_table.yview
        )

        scroll_x.config(
            command=self.result_table.xview
        )

        # ================= HEADINGS =================

        self.result_table.heading(
            "roll",
            text="Roll No."
        )

        self.result_table.heading(
            "name",
            text="Student Name"
        )

        self.result_table.heading(
            "course",
            text="Course"
        )

        self.result_table.heading(
            "subject",
            text="Subject"
        )

        self.result_table.heading(
            "marks",
            text="Marks Obtained"
        )

        self.result_table.heading(
            "full_marks",
            text="Full Marks"
        )

        # ================= COLUMN WIDTH =================

        self.result_table.column(
            "roll",
            width=130,
            anchor=CENTER
        )

        self.result_table.column(
            "name",
            width=190,
            anchor=CENTER
        )

        self.result_table.column(
            "course",
            width=160,
            anchor=CENTER
        )

        self.result_table.column(
            "subject",
            width=180,
            anchor=CENTER
        )

        self.result_table.column(
            "marks",
            width=170,
            anchor=CENTER
        )

        self.result_table.column(
            "full_marks",
            width=150,
            anchor=CENTER
        )

        self.result_table.pack(
            fill=BOTH,
            expand=True
        )

        # ================= LOAD DATA =================

        self.show_all()

    # =========================================================
    # DATABASE CONNECTION
    # =========================================================

    def connect_db(self):

        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="user",
            database="srms"
        )

    # =========================================================
    # SHOW ALL
    # =========================================================

    def show_all(self):

        try:

            con = self.connect_db()
            cur = con.cursor()

            # IMPORTANT:
            # ID/RID ko select nahi kar rahe.
            # Sirf wahi columns select kar rahe hain
            # jo Treeview mein hain.

            cur.execute(
                "SELECT roll, name, course, subject, marks, full_marks "
                "FROM result ORDER BY rid DESC"
            )

            rows = cur.fetchall()

            # Clear old data

            self.result_table.delete(
                *self.result_table.get_children()
            )

            # Insert new data

            for row in rows:

                self.result_table.insert(
                    "",
                    END,
                    values=row
                )

            cur.close()
            con.close()

        except mysql.connector.Error as ex:

            messagebox.showerror(
                "Database Error",
                f"Error due to:\n{str(ex)}"
            )

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to:\n{str(ex)}"
            )

    # =========================================================
    # SEARCH
    # =========================================================

    def search(self):

        search_roll = self.var_roll.get().strip()

        if search_roll == "":

            messagebox.showerror(
                "Error",
                "Please enter Roll No."
            )

            return

        try:

            con = self.connect_db()
            cur = con.cursor()

            # Same column order as Treeview

            cur.execute(
                "SELECT roll, name, course, subject, marks, full_marks "
                "FROM result "
                "WHERE roll=%s "
                "ORDER BY rid DESC",
                (search_roll,)
            )

            rows = cur.fetchall()

            # Clear old data

            self.result_table.delete(
                *self.result_table.get_children()
            )

            if len(rows) == 0:

                messagebox.showinfo(
                    "Result",
                    "No result found for this Roll No."
                )

            else:

                for row in rows:

                    self.result_table.insert(
                        "",
                        END,
                        values=row
                    )

            cur.close()
            con.close()

        except mysql.connector.Error as ex:

            messagebox.showerror(
                "Database Error",
                f"Error due to:\n{str(ex)}"
            )

        except Exception as ex:

            messagebox.showerror(
                "Error",
                f"Error due to:\n{str(ex)}"
            )


# =============================================================
# MAIN
# =============================================================

if __name__ == "__main__":

    root = Tk()

    obj = ViewResultClass(root)

    root.mainloop()