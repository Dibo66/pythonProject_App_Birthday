from tkinter import *
from testappAddpeople import AddPeople
from testappUpdate import Update
from testappDisplay import Display
from testappBirthday import Birthday
from tkinter import messagebox
import query_in_functions


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x585+600+80")
        self.title("My People")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/peoples.png')
        self.top_image_lable = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lable.place(x=130, y=25)

        self.heading = Label(self.top, text='My People', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=270, y=50)
###===============================================
        record_bd_today = query_in_functions.bday_persons()
        names_bd = []
        for row in record_bd_today:
            names_bd.append(row[1])

        listToStr = ', '.join(map(str, names_bd))
# ==========================
        self.date_lbl = Label(self.top, text="Birthday today: " + str(listToStr), font='arial 12 bold', fg='#ebb434', bg='white')
        self.date_lbl.place(x=40, y=110)
# ==========================

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listBox = Listbox(self.bottom, width=40, height=27)
        self.listBox.grid(row=0, column=0, padx=(40, 0))
        
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        persons = query_in_functions.read_Sqlite_Table()
        print(persons)
        count = 0

        for person in persons:
            self.listBox.insert(count, str(person[0]) + ". " + person[1] + " " + person[2])
            count += 1
        self.scroll.grid(row=0, column=1, sticky=N+S)

        # Buttons

        btnAdd = Button(self.bottom, text='Add', width=12, font='Sans 12 bold', command=self.add_people)
        btnAdd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btnUpdate = Button(self.bottom, text='Update', width=12, font='Sans 12 bold', command=self.update_function)
        btnUpdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btnDisplay = Button(self.bottom, text='Display', width=12, font='Sans 12 bold', command=self.display_person)
        btnDisplay.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btnDelete = Button(self.bottom, text='Delete', width=12, font='Sans 12 bold', command=self.delete_person)
        btnDelete.grid(row=0, column=2, padx=20, pady=130, sticky=N)
        # ===================
        btnBirthday = Button(self.bottom, text='Birthday', width=12, font='Sans 12 bold', command=self.birthday_persons)
        btnBirthday.grid(row=0, column=2, padx=20, pady=170, sticky=N)

    def birthday_persons(self):
        add_page = Birthday()

    # =====================
    def delete_person(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]

        str_for_mbox = "are you sure wanna delete", person.split(".")[1], "?"
        answer = messagebox.askquestion("Warning", str_for_mbox)

        if answer == 'yes':
            try:
                # query = "DELETE FROM addressbook WHERE person_id = {};".format(person_id)
                # cur.execute(query)
                # con.commit()
                query_in_functions.delete_Sqlite_Record(person_id)
                messagebox.showinfo("Success", "Deleted")
                self.destroy()

            except Exception as e:
                messagebox.showinfo("Info", str(e))

    def add_people(self):
        add_page = AddPeople()
        self.destroy()

    def update_function(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        updatepage = Update(person_id)
        self.destroy()

    def display_person(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        print(person_id)
        displaypage = Display(person_id)

