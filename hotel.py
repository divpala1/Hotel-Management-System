# Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.
from tkinter import *

# Terminal command to install PIL: pip install pillow
from PIL import Image, ImageTk

# Importing the 'Cust_Win' class from the 'customer.py'.
from customer import Cust_Win

# Importing the 'Room_Booking' class from the 'room.py'.
from room import Room_Booking

# Importing the 'Details' class from the 'details.py'.
from details import Details


# noinspection PyAttributeOutsideInit
class HotelManagementSystem:
    # 'root' is the name of the window of GUI (decided by the user, not predefined).
    # noinspection PyShadowingNames
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")

        # To be interpreted as, a window of width 1550, height 1080, starting from 0 for x-axis, and starting from 0 for y-axis. Note the symbols between each attribute.
        # self.root.geometry("'width'x'height'+'x-axis offset'+'y-axis offset'")
        self.root.geometry("1550x800+0+0")

        # ============================================= Image 1 ======================================================
        # The modifier r before the string tells Python that this is a raw string. In raw strings, the backslash is interpreted literally, not as an escape character.
        img1 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\hotel1.png")

        # ANTI-ALIAS removes the structural Padding from the Image around it
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)

        # A label widget can display either PhotoImage or BitmapImage objects.
        # Creating a photoimage object of the image.
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # This widget implements a display box where you can place text or images.
        # (master = parent window, image = image to be shown as label, bd = size of border, relief = appearance of a decorative border around the label)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ============================================= Logo ======================================================
        img2 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\logohotel.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ============================================= Title ======================================================
        lbl_title = Label(self.root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550)

        # ============================================= Main Frame ====================================================
        # The Frame widget is very important for the process of grouping and organizing other widgets in a somehow friendly way. It works like a container, which is responsible for arranging the position of other widgets.
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=210, width=1920, height=620)

        # ============================================= Menu ====================================================
        # Note that 'master = main_frame' for this label. Hence y=0.
        lbl_menu = Label(main_frame, text="Menu", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4,
                         relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ============================================= Button Frame ====================================================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=40, width=230, height=190)

        cust_btn = Button(btn_frame, text="Customer", width=20, command=self.cust_details, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, command=self.room_booking, text="Room", width=20, font=("times new roman", 14, "bold"), bg="black", fg="gold",
                          bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, command=self.room_details, text="Details", width=20, font=("times new roman", 14, "bold"), bg="black",
                             fg="gold", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="Report", width=20, font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="Logout", width=20, font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        # ============================================= Right Image ====================================================
        img3 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=231, y=0, width=1310, height=590)

        # ========================================== Images below buttons ===========================================
        img4 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\myh.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=230, width=230, height=210)

        img5 = Image.open(r"D:\Coding\Language stuff\Python\Projects\Hotel Management\Images\khana.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=440, width=230, height=190)

    def cust_details(self):
        # To activate this command when clicked on the customer button, 'command=self.cust_details' line is added to 'cust_btn'.
        # A Toplevel widget is used to create a window on top of all other windows. The Toplevel widget is used to provide some extra information to the user and also when our program deals with more than one application. These windows are directly organized and managed by the Window Manager and do not need to have any parent window associated with them every time.
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def room_booking(self):
        # To activate this command when clicked on the customer button, 'command=self.room_booking' line is added to 'room_btn'.
        # A Toplevel widget is used to create a window on top of all other windows. The Toplevel widget is used to provide some extra information to the user and also when our program deals with more than one application. These windows are directly organized and managed by the Window Manager and do not need to have any parent window associated with them every time.
        self.new_window = Toplevel(self.root)
        self.app = Room_Booking(self.new_window)

    def room_details(self):
        # To activate this command when clicked on the customer button, 'command=self.room_details' line is added to 'details_btn'.
        # A Toplevel widget is used to create a window on top of all other windows. The Toplevel widget is used to provide some extra information to the user and also when our program deals with more than one application. These windows are directly organized and managed by the Window Manager and do not need to have any parent window associated with them every time.
        self.new_window = Toplevel(self.root)
        self.app = Details(self.new_window)


if __name__ == '__main__':
    root = Tk()

    # Will open the window in maximised form.
    root.state('zoomed')

    obj = HotelManagementSystem(root)

    # 'mainloop()' is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed. Any code after this mainloop() method will not run.
    root.mainloop()
