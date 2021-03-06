from tkinter import *
from tkinter import messagebox
from datetime import datetime
import query_in_functions


class Update(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)
        self.geometry("650x585+600+100")
        self.title("Update person")
        self.resizable(False, False)
        print("person id = ", person_id)

        result = query_in_functions.read_person_Id(person_id)

        print(result)
        self.person_id = person_id
        person_name = result[1]
        person_surname = result[2]
        person_email = result[3]
        person_phone = result[4]
        person_address = result[5]
        person_birthdate = result[6]

        print("person name", person_name)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/peoples.png')
        self.top_image_lable = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lable.place(x=130, y=25)

        self.heading = Label(self.top, text='Update person'
                             , font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=270, y=50)

        # Name
        self.label_name = Label(self.bottom, text="Name", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=150, y=40)

        # Surname
        self.label_surname = Label(self.bottom, text="Surname", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.place(x=150, y=80)

        # email
        self.label_email = Label(self.bottom, text="Email", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=150, y=120)

        # phone number
        self.label_phone_number = Label(self.bottom, text="Pnone No.", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_phone_number.place(x=40, y=160)

        self.entry_phone_number = Entry(self.bottom, width=20, bd=4)
        self.entry_phone_number.insert(0, person_phone)
        self.entry_phone_number.place(x=150, y=160)

        # person_birthdate
        self.label_person_birthdate = Label(self.bottom, text="Birth:     Year", font='arial 12 bold', fg='white',
                                            bg='#fcc324')
        self.label_person_birthdate.place(x=40, y=200)

        self.entry_person_birthdate = Entry(self.bottom, width=10, bd=4)
        self.entry_person_birthdate.insert(0, person_birthdate)
        self.entry_person_birthdate.place(x=150, y=200)

        # address
        self.label_address = Label(self.bottom, text="Address", font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_address.place(x=40, y=240)

        self.entry_address = Text(self.bottom, width=30, height=4)
        self.entry_address.insert(1.0, person_address)
        self.entry_address.place(x=150, y=240)

        # Button
        button = Button(self.bottom, text="Update person", command=self.update_people)
        button.place(x=270, y=350)

    def update_people(self):
        id = self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone_number.get()
        birthday = self.entry_person_birthdate.get()
        address = self.entry_address.get(1.0, 'end-1c')

        birthdate = datetime.strptime(f"{birthday}", '%Y-%m-%d').date()
        print(birthdate)
# =============================================================

        query_in_functions.update_Sqlite_Table(name, surname, email, phone, address, birthdate, id)
        messagebox.showinfo("Success", "Contact Updated")
        self.destroy()
