from tkinter import *
from testAppButtons import MyButton
import query_in_functions


class Birthday(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x585+600+100")
        self.title("Birthday's today")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=350, bg='#ebb134')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/birthday.png')
        self.top_image_lable = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lable.place(x=130, y=25)

        self.heading = Label(self.top, text="Birthday's today", font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=270, y=50)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listBox = Listbox(self.bottom, width=40, height=27)
        self.listBox.grid(row=0, column=0, padx=(40, 0))

        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

#==============================================================
        persons = query_in_functions.bday_persons()

        print(len(persons))
        count = 0

        for person in persons:
            self.listBox.insert(count, str(person[0]) + ". " + person[1] + " " + person[3] + " " + person[4])
            count += 1
        self.scroll.grid(row=0, column=1, sticky=NS)

        btnSent = MyButton(self.bottom, text='Sent', command=self.email_person)
        btnSent.grid(row=0, column=2, padx=20, pady=10, sticky=N)

    def email_person(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        email_id = person.split(" ")[2]
        print(email_id)

        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        smtp_server = "smtp.gmail.com"
        port = 587
        email = "d???????06@gmail.com"  # the email where you sent the email
        password = input("Type your password and press enter: ")
        sent_to_email = f"{email_id}"  # for whom
        subject = "Test from Python"
        message = "This is a test email sent by Python. Isn't that cool?!"

        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = sent_to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, sent_to_email, text)
        print(f"Send mail to: {sent_to_email}")
        print("Successfully sent email and closing the server")
        server.quit()


