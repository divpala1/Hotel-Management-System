from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector  # pip install mysql-connector-python
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Room_Booking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1296x550+230+240")

        # ============================================= Variables ======================================================
        self.varContact = StringVar()
        self.varCheckIn = StringVar()
        self.varCheckOut = StringVar()
        self.varRoomType = StringVar()
        self.varRoom = StringVar()
        self.varMeal = StringVar()
        self.varNoOfDays = StringVar()
        self.varTaxPaid = StringVar()
        self.varCost = StringVar()
        self.varTotal = StringVar()

        # ============================================= Title ======================================================
        lbl_title = Label(self.root, text="Room Booking", font=("times new roman", 18, "bold"), bg="black", fg="gold",
                          bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ============================================= Logo ======================================================
        img2 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\logohotel.png")
        img2 = img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=50)

        # ============================================= Label Frame ======================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room details", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ============================================= Labels and Entries ======================================================

        # Customer Contact
        lblCustContact = Label(labelframeleft, text="Customer Contact: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblCustContact.grid(row=0, column=0, sticky=W)

        entryContact = ttk.Entry(labelframeleft, textvariable=self.varContact, width=14, font=("arial", 13, "bold"))
        entryContact.grid(row=0, column=1, sticky=W)

        # Fetch-data button
        btnFetchData = Button(labelframeleft, command=self.fetchContact, text="Fetch data", width=10,
                              font=("arial", 10, "bold"), bg="black",
                              fg="gold")
        btnFetchData.place(x=298, y=4)

        # Check-in date
        lblCheckIn = Label(labelframeleft, text="Check-in date: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblCheckIn.grid(row=1, column=0, sticky=W)

        entryCheckIn = ttk.Entry(labelframeleft, textvariable=self.varCheckIn, width=25, font=("arial", 13, "bold"))
        entryCheckIn.grid(row=1, column=1)

        # Check-out date
        lblCheckOut = Label(labelframeleft, text="Check-out date: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblCheckOut.grid(row=2, column=0, sticky=W)

        entryCheckOut = ttk.Entry(labelframeleft, textvariable=self.varCheckOut, width=25, font=("arial", 13, "bold"))
        entryCheckOut.grid(row=2, column=1)

        # Room type
        lblRoomType = Label(labelframeleft, text="Room type: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                       database="management")
        myCursor = conn.cursor()
        myCursor.execute("SELECT roomType FROM details")
        # Storing the data of SQL Table in a variable.
        roomTypes = myCursor.fetchall()

        comboRoomType = ttk.Combobox(labelframeleft, textvariable=self.varRoomType, font=("arial", 12, "bold"),
                                     width=23, state="readonly")
        comboRoomType["value"] = roomTypes
        comboRoomType.grid(row=3, column=1)
        # Assigning a default value from the tuple above.
        comboRoomType.current(0)

        # Available rooms
        lblRoom = Label(labelframeleft, text="Available Room: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoom.grid(row=4, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                       database="management")
        myCursor = conn.cursor()
        myCursor.execute("SELECT roomNo FROM details")
        # Storing the data of SQL Table in a variable.
        rooms = myCursor.fetchall()

        comboRoom = ttk.Combobox(labelframeleft, textvariable=self.varRoom, font=("arial", 12, "bold"),
                                     width=23, state="readonly")
        comboRoom["value"] = rooms
        comboRoom.grid(row=4, column=1)
        comboRoom.current(0)

        # Meal
        lblMeal = Label(labelframeleft, text="Meal: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        comboRoomType = ttk.Combobox(labelframeleft, textvariable=self.varMeal, font=("arial", 12, "bold"),
                                     width=23, state="readonly")
        comboRoomType["value"] = ("Breakfast", "Lunch")
        comboRoomType.grid(row=5, column=1)
        # Assigning a default value from the tuple above.
        comboRoomType.current(0)

        # Number of days of stay
        lblNoOfDays = Label(labelframeleft, text="No. of days: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        entryNoOfDays = ttk.Entry(labelframeleft, textvariable=self.varNoOfDays, width=25, font=("arial", 13, "bold"))
        entryNoOfDays.grid(row=6, column=1)

        # Cost
        lblSubTotal = Label(labelframeleft, text="Cost per night: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=7, column=0, sticky=W)

        entrySubTotal = ttk.Entry(labelframeleft, textvariable=self.varCost, width=25, font=("arial", 13, "bold"))
        entrySubTotal.grid(row=7, column=1)

        # Tax paid
        lblTaxPaid = Label(labelframeleft, text="Tax paid: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblTaxPaid.grid(row=8, column=0, sticky=W)

        entryTaxPaid = ttk.Entry(labelframeleft, textvariable=self.varTaxPaid, width=25, font=("arial", 13, "bold"))
        entryTaxPaid.grid(row=8, column=1)

        # Total cost
        lblTotalCost = Label(labelframeleft, text="Total cost: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        entryTotalCost = ttk.Entry(labelframeleft, textvariable=self.varTotal, width=25, font=("arial", 13, "bold"))
        entryTotalCost.grid(row=9, column=1)

        # ============================================= Bill button ======================================================
        btnBill = Button(labelframeleft, command=self.total, text="Bill", width=15, font=("arial", 13, "bold"),
                         bg="black", fg="gold")
        btnBill.place(x=130, y=355)

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

        # ============================================= Right side image ======================================================
        img3 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\bed.jpg")
        img3 = img3.resize((530, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=5, relief=RIDGE)
        lblimg.place(x=760, y=55, width=530, height=300)

        # ============================================= Table Frame for search system ======================================================
        tableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details", padx=2,
                                font=("times new roman", 12, "bold"))
        tableFrame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(tableFrame, text="Search By: ", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        # Storing the value of the combobox in a variable. Command given in the 'ttk.Combobox()' for attaching this variable is 'textvariable = self.varSearch'
        self.varSearch = StringVar()

        comboSearch = ttk.Combobox(tableFrame, textvariable=self.varSearch, font=("arial", 12, "bold"), width=20,
                                   state="readonly")
        comboSearch["value"] = ("Contact", "Room")
        comboSearch.grid(row=0, column=1)
        comboSearch.current(0)

        # Storing the value of text to a variable.
        self.txtSearch = StringVar()
        txtSearch = ttk.Entry(tableFrame, textvariable=self.txtSearch, width=25, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(tableFrame, command=self.searchData, text="Search", width=9, font=("arial", 12, "bold"),
                           bg="black", fg="gold")
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(tableFrame, command=self.fetchData, text="Show all", width=9, font=("arial", 12, "bold"),
                            bg="black", fg="gold")
        btnShowAll.grid(row=0, column=4, padx=1)

        # ============================================= Data Table ======================================================
        detailsTable = Frame(tableFrame, bd=2, relief=RIDGE)
        detailsTable.place(x=0, y=50, width=860, height=180)

        scrollX = ttk.Scrollbar(detailsTable, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(detailsTable, orient=VERTICAL)

        # A Treeview widget allows you to display data in both tabular and hierarchical structures.
        # These won't be displayed to the user.
        self.Room_Table = ttk.Treeview(detailsTable, column=(
            "contact", "checkInDate", "checkOutDate", "roomType", "Room", "meal", "noOfDays"),
                                       xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)

        # 'side=' will tell the place where scroll bar is to be placed. 'fill=' will fill the whole axis.
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        scrollX.config(command=self.Room_Table.xview)
        scrollY.config(command=self.Room_Table.yview)

        self.Room_Table.heading("contact", text="Contact")
        self.Room_Table.heading("checkInDate", text="Check-in date")
        self.Room_Table.heading("checkOutDate", text="Check-out date")
        self.Room_Table.heading("roomType", text="Room Type")
        self.Room_Table.heading("Room", text="Room available")
        self.Room_Table.heading("meal", text="Meal")
        self.Room_Table.heading("noOfDays", text="No. of days")

        self.Room_Table["show"] = "headings"
        # Setting the width of the columns.
        self.Room_Table.column("contact", width=110)
        self.Room_Table.column("checkInDate", width=110)
        self.Room_Table.column("checkOutDate", width=110)
        self.Room_Table.column("roomType", width=110)
        self.Room_Table.column("Room", width=110)
        self.Room_Table.column("meal", width=110)
        self.Room_Table.column("noOfDays", width=110)

        # 'fill=BOTH' will fill the table on both axes. 'expand=1' will adjust the names of columns according to size.
        self.Room_Table.pack(fill=BOTH, expand=1)
        self.Room_Table.bind("<ButtonRelease-1>", self.getCursor)
        self.fetchData()

    # ============================================= Add data ======================================================
    def addData(self):
        if self.varContact.get() == "" or self.varCheckIn.get() == "":
            messagebox.showerror("Error", "Filling all the fields is mandatory", parent=self.root)
        else:
            try:
                # 'connection' is abbreviated as 'conn'
                conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                               database="management")
                myCursor = conn.cursor()
                # Number of '%s' = number of columns in table.
                # In the 'execute()' command, we enter the SQL query.
                myCursor.execute("INSERT INTO room VALUES(%s, %s, %s, %s, %s, %s, %s)", (
                    # Chronology should be the same as the one defined in the treeview widget.
                    self.varContact.get(),
                    self.varCheckIn.get(),
                    self.varCheckOut.get(),
                    self.varRoomType.get(),
                    self.varRoom.get(),
                    self.varMeal.get(),
                    self.varNoOfDays.get()
                ))
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success", "Room booked", parent=self.root)

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

        self.varContact.set(row[0])
        self.varCheckIn.set(row[1])
        self.varCheckOut.set(row[2])
        self.varRoomType.set(row[3])
        self.varRoom.set(row[4])
        self.varMeal.set(row[5])
        self.varNoOfDays.set(row[6])

    # Function to update data.
    def updateData(self):
        if self.varContact.get() == "":
            messagebox.showerror("Error", "Kindly enter the mobile number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                           database="management")
            myCursor = conn.cursor()
            # As the data is being updated based on the reference number, the last argument passed is 'where Ref=%s'
            myCursor.execute(
                "UPDATE room SET checkIn=%s, checkOut=%s, roomType=%s, Room=%s, meal=%s, noOfDays=%s where contact=%s",
                (
                    self.varCheckIn.get(),
                    self.varCheckOut.get(),
                    self.varRoomType.get(),
                    self.varRoom.get(),
                    self.varMeal.get(),
                    self.varNoOfDays.get(),
                    self.varContact.get()
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
            query = "DELETE FROM room WHERE contact=%s"
            value = (self.varContact.get(),)
            myCursor.execute(query, value)
        else:
            if not deleteData:
                return

        conn.commit()
        self.fetchData()
        conn.close()

    def reset(self):
        self.varContact.set("")
        self.varCheckIn.set("")
        self.varCheckOut.set("")
        self.varRoom.set("")
        self.varMeal.set("")
        self.varNoOfDays.set("")
        self.varCost.set("")
        self.varTaxPaid.set("")
        self.varTotal.set("")

    # ============================================= Fetch data function ======================================================
    def fetchData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1", database="management")
        myCursor = conn.cursor()
        myCursor.execute("SELECT * FROM room")
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

    # ============================================= Fetch all data ======================================================
    def fetchContact(self):
        if self.varContact.get() == "":
            messagebox.showerror("Error", "Kindly enter a contact number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                           database="management")
            myCursor = conn.cursor()
            query = "SELECT Name FROM customer WHERE mobile=%s"
            value = (self.varContact.get(),)
            myCursor.execute(query, value)
            row = myCursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Number not found", parent=self.root)

            else:
                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=450, y=55, width=300, height=180)

                # ============================== Name ====================================
                lblName = Label(showDataFrame, text="Name: ", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row[0], font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                # ============================== Gender ====================================
                query = "SELECT Gender FROM customer WHERE mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblGender = Label(showDataFrame, text="Gender: ", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=30)

                # ============================== Email ====================================
                query = "SELECT Email FROM customer WHERE mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblEmail = Label(showDataFrame, text="Email: ", font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=60)

                # ============================== Nationality ====================================
                query = "SELECT Nationality FROM customer WHERE mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblNationality = Label(showDataFrame, text="Nationality: ", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=90)

                # ============================== Address ====================================
                query = "SELECT Address FROM customer WHERE mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblAddress = Label(showDataFrame, text="Address: ", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl = Label(showDataFrame, text=row[0], font=("arial", 12, "bold"))
                lbl.place(x=90, y=120)

                conn.commit()
                conn.close()

    # Function for searching an entry based on the parameter entered by the user.
    def searchData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                       database="management")
        myCursor = conn.cursor()

        myCursor.execute(
            "SELECT * FROM room WHERE " + str(self.varSearch.get()) + "=" + str(self.txtSearch.get()))
        rows = myCursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
        conn.commit()
        conn.close()

    # Function to calculate number of days between check-in and check-out date.
    def total(self):
        inDate = self.varCheckIn.get()
        outDate = self.varCheckOut.get()

        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")

        self.varNoOfDays.set(abs(outDate - inDate).days)

        meal = 0
        room = 0
        cost = 0
        tax = 0
        total = 0

        if self.varMeal.get() == "Breakfast":
            meal = 300.00
            cost += meal

        if self.varMeal.get() == "Lunch":
            meal = 500.00
            cost += meal

        if self.varRoomType.get() == "Single":
            room = 1000.00
            cost += room

        if self.varRoomType.get() == "Double":
            room = 2000.00
            cost += room

        if self.varRoomType.get() == "Luxury":
            room = 3000.00
            cost += room

        days = float(self.varNoOfDays.get())
        cost = float((meal + room))
        self.varCost.set(cost)
        cost = float(cost * days)

        tax = cost * 0.18  # 18% tax
        total = "Rs. " + str("%.2f" % (cost + tax))
        tax = "Rs. " + str("%.2f" % tax)

        self.varTaxPaid.set(tax)
        self.varTotal.set(total)


if __name__ == '__main__':
    root = Tk()
    obj = Room_Booking(root)
    root.mainloop()
