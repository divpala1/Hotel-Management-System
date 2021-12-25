from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector  # pip install mysql-connector-python
from tkinter import messagebox


class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1296x550+230+240")

        # ============================================= Title ======================================================
        lbl_title = Label(self.root, text="Details", font=("times new roman", 18, "bold"), bg="black", fg="gold",
                          bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ============================================= Logo ======================================================
        img2 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\logohotel.png")
        img2 = img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=50)

        # ============================================= Label Frame ======================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Adding new room", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ============================================= Labels and Entries ======================================================
        # Floor
        lblFloor = Label(labelframeleft, text="Floor: ", font=("arial", 18, "bold"), padx=2, pady=6)
        lblFloor.grid(row=0, column=0, sticky=W)

        self.varFloor = StringVar()

        entryFloor = ttk.Entry(labelframeleft, textvariable=self.varFloor, width=20, font=("arial", 15, "bold"))
        entryFloor.grid(row=0, column=1, sticky=W)

        # Room number
        lblRoomNo = Label(labelframeleft, text="Room number: ", font=("arial", 18, "bold"), padx=2, pady=6)
        lblRoomNo.grid(row=1, column=0, sticky=W)

        self.varRoomNo = StringVar()

        entryRoomNo = ttk.Entry(labelframeleft, textvariable=self.varRoomNo, width=20, font=("arial", 15, "bold"))
        entryRoomNo.grid(row=1, column=1, sticky=W)

        # Room type
        lblRoomType = Label(labelframeleft, text="Room type: ", font=("arial", 18, "bold"), padx=2, pady=6)
        lblRoomType.grid(row=2, column=0, sticky=W)

        self.varRoomType = StringVar()

        comboRoomType = ttk.Combobox(labelframeleft, textvariable=self.varRoomType, font=("arial", 12, "bold"),
                                     width=23, state="readonly")
        comboRoomType["value"] = ("Single", "Double", "Luxury")
        comboRoomType.grid(row=2, column=1)
        # Assigning a default value from the tuple above.
        comboRoomType.current(0)

        # ============================================= Buttons ======================================================
        btnFrame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnFrame.place(x=0, y=400, width=412, height=40)

        # Remember to not add parenthesis behind the function name in 'command=' field.
        btnAdd = Button(btnFrame, command=self.addData, text="Add", width=9, font=("arial", 12, "bold"), bg="black",
                        fg="gold")
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btnFrame, command=self.updateData, text="Update", width=9, font=("arial", 12, "bold"),
                           bg="black", fg="gold")
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btnFrame, command=self.deleteData, text="Delete", width=9, font=("arial", 12, "bold"),
                           bg="black", fg="gold")
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btnFrame, command=self.reset, text="Reset", width=9, font=("arial", 12, "bold"), bg="black",
                          fg="gold")
        btnReset.grid(row=0, column=3, padx=1)

        # ============================================= Table Frame for search system ======================================================
        tableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show room details", padx=2,
                                font=("times new roman", 12, "bold"))
        tableFrame.place(x=435, y=55, width=855, height=260)

        scrollX = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(tableFrame, orient=VERTICAL)

        # A Treeview widget allows you to display data in both tabular and hierarchical structures.
        # These won't be displayed to the user.
        self.Room_Table = ttk.Treeview(tableFrame, column=("floor", "roomNo", "roomType"), xscrollcommand=scrollX.set,
                                       yscrollcommand=scrollY.set)

        # 'side=' will tell the place where scroll bar is to be placed. 'fill=' will fill the whole axis.
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        scrollX.config(command=self.Room_Table.xview)
        scrollY.config(command=self.Room_Table.yview)

        self.Room_Table.heading("floor", text="Floor")
        self.Room_Table.heading("roomNo", text="Room number")
        self.Room_Table.heading("roomType", text="Room type")

        self.Room_Table["show"] = "headings"

        # 'fill=BOTH' will fill the table on both axes. 'expand=1' will adjust the names of columns according to size.
        self.Room_Table.pack(fill=BOTH, expand=1)
        self.Room_Table.bind("<ButtonRelease-1>", self.getCursor)
        self.fetchData()

    # ============================================= Add data ======================================================
    def addData(self):
        if self.varFloor.get() == "" or self.varRoomNo.get() == "":
            messagebox.showerror("Error", "Filling all the fields is mandatory", parent=self.root)
        else:
            try:
                # 'connection' is abbreviated as 'conn'
                conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                               database="management")
                myCursor = conn.cursor()
                # Number of '%s' = number of columns in table.
                # In the 'execute()' command, we enter the SQL query.
                myCursor.execute("INSERT INTO details VALUES(%s, %s, %s)", (
                    # Chronology should be the same as the one defined in the treeview widget.
                    self.varFloor.get(),
                    self.varRoomNo.get(),
                    self.varRoomType.get()
                ))
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success", "New room added", parent=self.root)

            except Exception as es:
                # 'Ref' is the primary key in the table. Hence no duplicate reference numbers will be allowed.
                messagebox.showwarning("Warning", f"Something went wrong while entering the data. {str(es)}",
                                       parent=self.root)

    # Function to show data on the left window when clicked in the right window.
    def getCursor(self, event=""):
        # 'treeview.focus()' will output a dictionary, from which you can then easily retrieve individual values.
        cursorRow = self.Room_Table.focus()
        content = self.Room_Table.item(cursorRow)
        row = content["values"]

        self.varFloor.set(row[0])
        self.varRoomNo.set(row[1])
        self.varRoomType.set(row[2])

    # Function to update data.
    def updateData(self):
        if self.varFloor.get() == "":
            messagebox.showerror("Error", "Kindly enter the floor number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                           database="management")
            myCursor = conn.cursor()
            # As the data is being updated based on the room number, the last argument passed is 'where roomNo=%s'
            myCursor.execute(
                "UPDATE details SET floor=%s, roomType=%s where roomNo=%s",
                (
                    self.varFloor.get(),
                    self.varRoomType.get(),
                    self.varRoomNo.get()
                ))
            conn.commit()
            self.fetchData()
            conn.close()
            messagebox.showinfo("Success", "Room details have been updated", parent=self.root)

    # Function to delete data.
    def deleteData(self):
        deleteData = messagebox.askyesno("Confirmation required", "Do you wish to delete this entry?",
                                         parent=self.root)

        if deleteData > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                           database="management")
            myCursor = conn.cursor()
            # Alternative way to run a query.
            query = "DELETE FROM details WHERE roomNo=%s"
            value = (self.varRoomNo.get(),)
            myCursor.execute(query, value)
        else:
            if not deleteData:
                return

        conn.commit()
        self.fetchData()
        conn.close()

    def reset(self):
        self.varFloor.set("")
        self.varRoomNo.set("")

    # ============================================= Fetch data function ======================================================
    def fetchData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                       database="management")
        myCursor = conn.cursor()
        myCursor.execute("SELECT * FROM details")
        # Storing the data of SQL Table in a variable.
        rows = myCursor.fetchall()

        if len(rows) != 0:
            # Deleting all the rows in 'self.Room_Table'. Otherwise the previous data will be printed again for each time new data is added.
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                # Inserting the data of SQL table from the variable 'row', to the Treeview widget table so that it can be displayed.
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == '__main__':
    root = Tk()
    obj = Details(root)
    root.mainloop()
