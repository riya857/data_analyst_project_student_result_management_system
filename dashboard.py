from tkinter import *
from tkinter import messagebox
import time


# =========================================================
# DASHBOARD
# =========================================================

class RMS:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x700+80+40")
        self.root.resizable(False, False)

        # ================= TITLE =================

        title = Label(
            self.root,
            text="Student Result Management System",
            font=("times new roman", 30, "bold"),
            bg="#17202A",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=70)

        # ================= MENU =================

        menu = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 12, "bold"),
            bg="white",
            bd=2
        )
        menu.place(x=20, y=80, width=1160, height=80)

        # ================= COURSE =================
        Button(
            menu,
            text="Course",
            command=self.open_course,
            font=("times new roman", 14, "bold"),
            bg="#172A65",
            fg="white",
            cursor="hand2"
        ).place(x=15, y=15, width=170, height=45)

        # ================= STUDENT =================

        Button(
            menu,
            text="Student",
            command=self.open_student,
            font=("times new roman", 14, "bold"),
            bg="#172A65",
            fg="white",
            cursor="hand2"
        ).place(x=195, y=15, width=170, height=45)

        # ================= RESULT =================

        Button(
            menu,
            text="Result",
            command=self.open_result,
            font=("times new roman", 14, "bold"),
            bg="#172A65",
            fg="white",
            cursor="hand2"
        ).place(x=375, y=15, width=170, height=45)

        # ================= VIEW RESULT =================

        Button(
            menu,
            text="View Student Result",
            command=self.open_report,
            font=("times new roman", 13, "bold"),
            bg="#172A65",
            fg="white",
            cursor="hand2"
        ).place(x=555, y=15, width=190, height=45)

        # ================= LOGOUT =================

        Button(
            menu,
            text="Logout",
            command=self.logout,
            font=("times new roman", 14, "bold"),
            bg="#172A65",
            fg="white",
            cursor="hand2"
        ).place(x=755, y=15, width=150, height=45)

        # ================= EXIT =================

        Button(
            menu,
            text="Exit",
            command=self.exit_app,
            font=("times new roman", 14, "bold"),
            bg="#172A65",
            fg="white",
            cursor="hand2"
        ).place(x=915, y=15, width=150, height=45)

        # ================= CLOCK =================

        clock_frame = Frame(
            self.root,
            bg="#17202A",
            bd=2,
            relief=RIDGE
        )
        clock_frame.place(x=30, y=180, width=310, height=350)

        Label(
            clock_frame,
            text="Analog Clock",
            font=("times new roman", 22, "bold"),
            bg="#17202A",
            fg="white"
        ).pack(pady=15)

        self.clock = Label(
            clock_frame,
            font=("times new roman", 25, "bold"),
            bg="#17202A",
            fg="#00FFFF"
        )
        self.clock.pack(pady=70)

        self.update_clock()

        # ================= DASHBOARD IMAGE AREA =================

        image_frame = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )
        image_frame.place(x=360, y=180, width=800, height=350)

        canvas = Canvas(
            image_frame,
            width=790,
            height=340,
            bg="#F7F7F7",
            highlightthickness=0
        )
        canvas.pack()

        # Light blue background

        canvas.create_rectangle(
            20, 20, 770, 320,
            fill="#E8F4FA",
            outline=""
        )

        # ================= BOOKS ON TOP =================

        canvas.create_rectangle(
            130, 65, 170, 115,
            fill="#E74C3C",
            outline=""
        )

        canvas.create_rectangle(
            175, 55, 205, 115,
            fill="#F39C12",
            outline=""
        )

        canvas.create_rectangle(
            210, 60, 240, 115,
            fill="#8E44AD",
            outline=""
        )

        canvas.create_polygon(
            250, 50,
            275, 45,
            300, 115,
            275, 115,
            fill="#3498DB",
            outline=""
        )

        # ================= TOP SHELF =================

        canvas.create_line(
            90, 120, 480, 120,
            fill="#17202A",
            width=5
        )

        # ================= APPLE =================

        canvas.create_oval(
            115, 145, 165, 180,
            fill="#D9534F",
            outline=""
        )

        canvas.create_line(
            140, 145, 145, 133,
            width=4
        )

        canvas.create_oval(
            145, 132, 160, 140,
            fill="#27AE60",
            outline=""
        )

        # ================= BOOKS LEFT =================

        canvas.create_rectangle(
            70, 190, 260, 205,
            fill="#F5B041",
            outline=""
        )

        canvas.create_rectangle(
            60, 210, 270, 225,
            fill="#E67E22",
            outline=""
        )

        canvas.create_rectangle(
            75, 230, 280, 245,
            fill="#F4D03F",
            outline=""
        )

        # ================= COMPUTER =================

        canvas.create_rectangle(
            300, 145, 555, 265,
            fill="#172A65",
            outline="#172A65",
            width=5
        )

        canvas.create_rectangle(
            320, 160, 535, 245,
            fill="#5DADE2",
            outline=""
        )

        canvas.create_polygon(
            390, 180,
            390, 225,
            455, 202,
            fill="#2874A6",
            outline=""
        )

        canvas.create_rectangle(
            400, 265, 455, 280,
            fill="#172A65",
            outline=""
        )

        canvas.create_rectangle(
            375, 280, 480, 290,
            fill="#172A65",
            outline=""
        )

        # ================= PEN HOLDER =================

        canvas.create_rectangle(
            570, 215, 620, 270,
            fill="#2874A6",
            outline=""
        )

        canvas.create_line(
            580, 220, 560, 175,
            fill="#8E44AD",
            width=5
        )

        canvas.create_line(
            595, 220, 590, 165,
            fill="#E74C3C",
            width=5
        )

        canvas.create_line(
            610, 220, 625, 175,
            fill="#F39C12",
            width=5
        )

        # ================= TABLE LAMP =================

        canvas.create_polygon(
            620, 125,
            710, 145,
            680, 175,
            635, 165,
            fill="#E74C3C",
            outline=""
        )

        canvas.create_line(
            680, 160, 735, 195,
            fill="#922B21",
            width=6
        )

        canvas.create_line(
            735, 195, 690, 250,
            fill="#922B21",
            width=6
        )

        canvas.create_line(
            690, 250, 650, 280,
            fill="#922B21",
            width=6
        )

        canvas.create_oval(
            625, 275, 720, 295,
            fill="#922B21",
            outline=""
        )

        # ================= TABLE LINE =================

        canvas.create_line(
            40, 300, 750, 300,
            fill="#17202A",
            width=5
        )

        # ================= TOTAL BOXES =================

        Label(
            self.root,
            text="Total Students\n\n[ 3 ]",
            font=("times new roman", 18, "bold"),
            bg="#F15B3A",
            fg="white"
        ).place(
            x=30, y=550,
            width=350,
            height=110
        )

        Label(
            self.root,
            text="Total Course\n\n[ 3 ]",
            font=("times new roman", 18, "bold"),
            bg="#2196D3",
            fg="white"
        ).place(
            x=405, y=550,
            width=350,
            height=110
        )

        Label(
            self.root,
            text="Total Results\n\n[ 3 ]",
            font=("times new roman", 18, "bold"),
            bg="#1687C8",
            fg="white"
        ).place(
            x=780, y=550,
            width=380,
            height=110
        )

        # ================= FOOTER =================

        Label(
            self.root,
            text="Project Name: Student Result Management System",
            font=("times new roman", 14, "bold"),
            bg="#172A65",
            fg="white"
        ).place(
            x=0, y=665,
            relwidth=1,
            height=35
        )

    # =========================================================
    # COURSE
    # =========================================================

    def open_course(self):

        try:

            from courseclass import courseclass

            win = Toplevel(self.root)

            courseclass(win)

        except Exception as e:

            messagebox.showerror(
                "Course Error",
                str(e)
            )

    # =========================================================
    # STUDENT
    # =========================================================

    def open_student(self):

        try:

            from student import StudentClass

            win = Toplevel(self.root)

            StudentClass(win)

        except Exception as e:

            messagebox.showerror(
                "Student Error",
                str(e)
            )

    # =========================================================
    # RESULT
    # =========================================================

    def open_result(self):

        try:

            from result import ResultClass

            win = Toplevel(self.root)

            ResultClass(win)

        except Exception as e:

            messagebox.showerror(
                "Result Error",
                str(e)
            )

    # =========================================================
    # VIEW RESULT
    # =========================================================

    def open_report(self):

        try:

            from view_student_result import ViewResultClass

            win = Toplevel(self.root)

            ViewResultClass(win)

        except Exception as e:

            messagebox.showerror(
                "View Result Error",
                str(e)
            )

    # =========================================================
    # CLOCK
    # =========================================================

    def update_clock(self):

        current_time = time.strftime("%I:%M:%S %p")

        self.clock.config(
            text=current_time
        )

        self.root.after(
            1000,
            self.update_clock
        )

    # =========================================================
    # LOGOUT
    # =========================================================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if answer:

            self.root.destroy()

    # =========================================================
    # EXIT
    # =========================================================

    def exit_app(self):

        answer = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if answer:

            self.root.destroy()


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    root = Tk()

    obj = RMS(root)

    root.mainloop()