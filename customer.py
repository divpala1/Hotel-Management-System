from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector  # pip install mysql-connector-python
import random
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1296x550+230+240")

        # ============================================= Variables ======================================================
        # Variable to generate random Reference numbers. Since we don't need to perform any calculations, StringVar is used.
        self.varRef = StringVar()
        x = random.randint(1000, 9999)
        self.varRef.set(str(x))

        # StringVar() allows you to easily track tkinter variables and see if they have been read, overwritten, or if they even exist which you can't easily do with just a typical a = 'hello'
        # All these variables attached to the entry field by command: 'textvariable = self.variableName'
        self.varCustName = StringVar()
        self.varMother = StringVar()
        self.varGender = StringVar()
        self.varPost = StringVar()
        self.varMobile = StringVar()
        self.varEmail = StringVar()
        self.varNationality = StringVar()
        self.varAddress = StringVar()
        self.varidProof = StringVar()
        self.varidNumber = StringVar()

        # ============================================= Title ======================================================
        lbl_title = Label(self.root, text="Add Customer Details", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ============================================= Logo ======================================================
        img2 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\logohotel.png")
        img2 = img2.resize((100, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=50)

        # ============================================= Label Frame ======================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer details", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ============================================= Labels and Entries ======================================================

        # Customer reference
        lblCustRef = Label(labelframeleft, text="Customer Reference: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblCustRef.grid(row=0, column=0, sticky=W)

        # 'state="readonly"' will prevent the user from altering the randomly generated reference number.
        entryRef = ttk.Entry(labelframeleft, textvariable=self.varRef, width=25, font=("arial", 13, "bold"),
                             state="readonly")
        entryRef.grid(row=0, column=1)

        # Customer Name
        cName = Label(labelframeleft, text="Customer Name: ", font=("arial", 12, "bold"), padx=2, pady=6)
        cName.grid(row=1, column=0, sticky=W)

        txtCName = ttk.Entry(labelframeleft, textvariable=self.varCustName, width=25, font=("arial", 13, "bold"))
        txtCName.grid(row=1, column=1)

        # Mother's Name
        lblMname = Label(labelframeleft, text="Mother's Name: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMname.grid(row=2, column=0, sticky=W)

        txtMName = ttk.Entry(labelframeleft, textvariable=self.varMother, width=25, font=("arial", 13, "bold"))
        txtMName.grid(row=2, column=1)

        # Gender combobox
        lblGender = Label(labelframeleft, text="Gender: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblGender.grid(row=3, column=0, sticky=W)

        # Drop-down menu for gender.
        # 'state="readonly"' will prevent users from typing in the Combobox.
        comboGender = ttk.Combobox(labelframeleft, textvariable=self.varGender, font=("arial", 12, "bold"), width=23,
                                   state="readonly")
        comboGender["value"] = ("Male", "Female", "Other")
        comboGender.grid(row=3, column=1)
        # Assigning a default value from the tuple above.
        comboGender.current(0)

        # Postcode
        lblPostcode = Label(labelframeleft, text="Post Code: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostcode.grid(row=4, column=0, sticky=W)

        txtPostcode = ttk.Entry(labelframeleft, textvariable=self.varPost, width=25, font=("arial", 13, "bold"))
        txtPostcode.grid(row=4, column=1)

        # Mobile Number
        lblMobile = Label(labelframeleft, text="Mobile Number: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft, textvariable=self.varMobile, width=25, font=("arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        # E-mail
        lblEmail = Label(labelframeleft, text="E-mail: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, textvariable=self.varEmail, width=25, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(labelframeleft, text="Nationality: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        comboNationality = ttk.Combobox(labelframeleft, textvariable=self.varNationality, font=("arial", 12, "bold"),
                                        width=23, state="readonly")
        comboNationality["value"] = ("Indian", "American", "British")
        comboNationality.grid(row=7, column=1)
        comboNationality.current(0)

        # Id proof type combobox
        lblIdProof = Label(labelframeleft, text="Id Proof Type: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        comboID = ttk.Combobox(labelframeleft, textvariable=self.varidProof, font=("arial", 12, "bold"), width=23,
                               state="readonly")
        comboID["value"] = ("Aadhaar card", "Driving license", "Passport")
        comboID.grid(row=8, column=1)
        comboID.current(0)

        # ID number
        lblIdNumber = Label(labelframeleft, text="Id Number: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.varidNumber, width=25, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, text="Address: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        txtAddress = ttk.Entry(labelframeleft, textvariable=self.varAddress, width=25, font=("arial", 13, "bold"))
        txtAddress.grid(row=10, column=1)

        # ============================================= Buttons ======================================================
        btnFrame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btnFrame.place(x=0, y=400, width=412, height=40)

        # Remember to not add parenthesis behind the function name in 'command=' field.
        btnAdd = Button(btnFrame, text="Add", command=self.addData, width=9, font=("arial", 12, "bold"), bg="black",
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

        # ============================================= Table Frame for searching ======================================================
        tableFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details", padx=2,
                                font=("times new roman", 12, "bold"))
        tableFrame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(tableFrame, text="Search By: ", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        # Storing the value of the combobox in a variable. Command given in the 'ttk.Combobox()' for attaching this variable is 'textvariable = self.varSearch'
        self.varSearch = StringVar()

        comboSearch = ttk.Combobox(tableFrame, textvariable=self.varSearch, font=("arial", 12, "bold"), width=20,
                                   state="readonly")
        comboSearch["value"] = ("Mobile", "Ref")
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
        detailsTable.place(x=0, y=50, width=860, height=350)

        scrollX = ttk.Scrollbar(detailsTable, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(detailsTable, orient=VERTICAL)

        # A Treeview widget allows you to display data in both tabular and hierarchical structures.
        # These won't be displayed to the user.
        self.Cust_Details_Table = ttk.Treeview(detailsTable, column=(
            "Ref", "Name", "Mother", "Gender", "Post", "Mobile", "Email", "Nationality", "idProof", "idNumber",
            "Address"),
                                               xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)

        # 'side=' will tell the place where scroll bar is to be placed. 'fill=' will fill the whole axis.
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        scrollX.config(command=self.Cust_Details_Table.xview)
        scrollY.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref", text="Reference number")
        self.Cust_Details_Table.heading("Name", text="Name")
        self.Cust_Details_Table.heading("Mother", text="Mother's Name")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("Post", text="Postcode")
        self.Cust_Details_Table.heading("Mobile", text="Mobile number")
        self.Cust_Details_Table.heading("Email", text="E-mail")
        self.Cust_Details_Table.heading("Nationality", text="Nationality")
        self.Cust_Details_Table.heading("idProof", text="ID Proof")
        self.Cust_Details_Table.heading("idNumber", text="ID number")
        self.Cust_Details_Table.heading("Address", text="Address")

        self.Cust_Details_Table["show"] = "headings"
        # Setting the width of the columns.
        self.Cust_Details_Table.column("Ref", width=110)
        self.Cust_Details_Table.column("Name", width=110)
        self.Cust_Details_Table.column("Mother", width=110)
        self.Cust_Details_Table.column("Gender", width=110)
        self.Cust_Details_Table.column("Post", width=110)
        self.Cust_Details_Table.column("Mobile", width=110)
        self.Cust_Details_Table.column("Email", width=110)
        self.Cust_Details_Table.column("Nationality", width=110)
        self.Cust_Details_Table.column("idProof", width=110)
        self.Cust_Details_Table.column("idNumber", width=110)
        self.Cust_Details_Table.column("Address", width=110)

        # 'fill=BOTH' will fill the table on both axes. 'expand=1' will adjust the names of columns according to size.
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.getCursor)
        self.fetchData()

    # Function to add data in the SQL table.
    def addData(self):
        if self.varMobile.get() == "" or self.varMother.get() == "":
            messagebox.showerror("Error", "Filling all the fields is mandatory", parent=self.root)
        else:
            try:
                # 'connection' is abbreviated as 'conn'
                conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                               database="management")
                myCursor = conn.cursor()
                # Number of '%s' = number of columns in table.
                # In the 'execute()' command, we enter the SQL query.
                myCursor.execute("insert into customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    # Chronology should be the same as the one defined in the treeview widget.
                    self.varRef.get(),
                    self.varCustName.get(),
                    self.varMother.get(),
                    self.varGender.get(),
                    self.varPost.get(),
                    self.varMobile.get(),
                    self.varEmail.get(),
                    self.varNationality.get(),
                    self.varidProof.get(),
                    self.varidNumber.get(),
                    self.varAddress.get()
                ))
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added.", parent=self.root)

            except Exception as es:
                # 'Ref' is the primary key in the table. Hence no duplicate reference numbers will be allowed.
                messagebox.showwarning("Warning", f"Something went wrong while entering the data. {str(es)}",
                                       parent=self.root)

    # Function to show data from SQL table in the right window.
    def fetchData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1", database="management")
        myCursor = conn.cursor()
        myCursor.execute("SELECT * FROM customer")
        # Storing the data of SQL Table in a variable.
        rows = myCursor.fetchall()

        if len(rows) != 0:
            # Deleting all the rows in 'self.Cust_Details_Table'. Otherwise the previous data will be printed again for each time new data is added.
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                # Inserting the data of SQL table from the variable 'row', to the Treeview widget table so that it can be displayed.
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Function to show data on the left window when clicked in the right window.
    def getCursor(self, event=""):
        # 'treeview.focus()' will output a dictionary, from which you can then easily retrieve individual values.
        cursorRow = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursorRow)
        row = content["values"]

        self.varRef.set(row[0])
        self.varCustName.set(row[1])
        self.varMother.set(row[2])
        self.varGender.set(row[3])
        self.varPost.set(row[4])
        self.varMobile.set(row[5])
        self.varEmail.set(row[6])
        self.varNationality.set(row[7])
        self.varidProof.set(row[8])
        self.varidNumber.set(row[9])
        self.varAddress.set(row[10])

    # Function to update data.
    def updateData(self):
        if self.varMobile.get() == "":
            messagebox.showerror("Error", "Kindly enter the mobile number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                           database="management")
            myCursor = conn.cursor()
            # As the data is being updated based on the reference number, the last argument passed is 'where Ref=%s'
            myCursor.execute(
                "UPDATE customer SET Name=%s, Mother=%s, Gender=%s, Postcode=%s, Mobile=%s, Email=%s, Nationality=%s, IDproof=%s, IDnumber=%s, Address=%s where Ref=%s",
                (
                    self.varCustName.get(),
                    self.varMother.get(),
                    self.varGender.get(),
                    self.varPost.get(),
                    self.varMobile.get(),
                    self.varEmail.get(),
                    self.varNationality.get(),
                    self.varidProof.get(),
                    self.varidNumber.get(),
                    self.varAddress.get(),
                    self.varRef.get()
                ))
            conn.commit()
            self.fetchData()
            conn.close()
            messagebox.showinfo("Success", "Customer details have been updated", parent=self.root)

    # Function to delete data.
    def deleteData(self):
        deleteData = messagebox.askyesno("Confirmation required", "Do you wish to delete this entry?", parent=self.root)
        if deleteData > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1",
                                           database="management")
            myCursor = conn.cursor()
            # Alternative way to run a query.
            query = "DELETE FROM customer WHERE Ref=%s"
            value = (self.varRef.get(),)
            myCursor.execute(query, value)
        else:
            if not deleteData:
                return

        conn.commit()
        self.fetchData()
        conn.close()

    def reset(self):
        self.varRef.set(str(random.randint(1000, 9999)))
        self.varCustName.set("")
        self.varMother.set("")
        self.varPost.set("")
        self.varMobile.set("")
        self.varEmail.set("")
        self.varidNumber.set("")
        self.varAddress.set("")

    # Function for searching an entry based on the parameter entered by the user.
    def searchData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Saitamaa1", database="management")
        myCursor = conn.cursor()

        myCursor.execute("SELECT * FROM customer WHERE " + str(self.varSearch.get()) + "=" + str(self.txtSearch.get()))
        rows = myCursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
