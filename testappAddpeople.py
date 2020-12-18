from tkinter import *
from tkinter import messagebox
from datetime import datetime
import query_in_functions



class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x600+600+100")
        self.title("Add new Person")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/peoples.png')
        self.top_image_lable = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lable.place(x=130, y=25)

        self.heading = Label(self.top, text='Add new person'
                             , font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=270, y=50)

        # Name
        self.label_name = Label(self.bottom, text="Name", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, "enter Name")
        self.entry_name.place(x=150, y=40)

        # Surname
        self.label_surname = Label(self.bottom, text="Surname", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, "enter Surname")
        self.entry_surname.place(x=150, y=80)

        # email
        self.label_email = Label(self.bottom, text="Email", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, "enter Email")
        self.entry_email.place(x=150, y=120)

        # phone number
        self.label_phone_number = Label(self.bottom, text="Pnone No.", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_phone_number.place(x=40, y=160)

        self.entry_phone_number = Entry(self.bottom, width=20, bd=4)
        self.entry_phone_number.insert(0, "Phone No.")
        self.entry_phone_number.place(x=150, y=160)

        # person_year
        self.label_person_year = Label(self.bottom, text="Birth:     Year", font='arial 12 bold', fg='white', bg='#fcc324')
        self.label_person_year.place(x=40, y=200)

        self.entry_person_year = Entry(self.bottom, width=10, bd=4)
        self.entry_person_year.insert(0, "Year")
        self.entry_person_year.place(x=150, y=200)

        # person_mont
        self.label_person_mont = Label(self.bottom, text="Month", font='arial 12 bold', fg='white', bg='#fcc324')
        self.label_person_mont.place(x=225, y=200)

        self.entry_person_mont = Entry(self.bottom, width=10, bd=4)
        self.entry_person_mont.insert(0, "Mont")
        self.entry_person_mont.place(x=280, y=200)

        # person_day
        self.label_person_day = Label(self.bottom, text="Day", font='arial 12 bold', fg='white', bg='#fcc324')
        self.label_person_day.place(x=355, y=200)

        self.entry_person_day = Entry(self.bottom, width=10, bd=4)
        self.entry_person_day.insert(0, "Day")
        self.entry_person_day.place(x=395, y=200)

        # address
        self.label_address = Label(self.bottom, text="Address", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_address.place(x=40, y=240)

        self.entry_address = Text(self.bottom, width=30, height=4)
        self.entry_address.place(x=150, y=240)

        # Button
        button = Button(self.bottom, text="add person", command=self.add_people)
        button.place(x=270, y=450)

    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone_number.get()
        year = self.entry_person_year.get()
        month = self.entry_person_mont.get()
        day = self.entry_person_day.get()
        address = self.entry_address.get(1.0, 'end-1c')

        if name and surname and email and phone and year and month and day and address != "":
            try:
                birthdate = datetime.strptime(f"{year}-{month}-{day}", '%Y-%m-%d').date()

                # add to database
                query_in_functions.insert_person(name, surname, email, phone, birthdate, address)
                messagebox.showinfo("Success", "Contact added")
                self.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please complete the required field", icon='warning')


