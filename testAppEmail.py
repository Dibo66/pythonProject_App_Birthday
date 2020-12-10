import smtplib, ssl
import sqlite3

#======================
con = sqlite3.connect('../pythonProject/test_appBirthday/database.db')

emails_bd_today = []
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM addressbook WHERE SUBSTR(person_birthdate, 6) = SUBSTR((SELECT date('now','localtime')), 6);")
    for row in cur.fetchall():
        email_bd_today = row[3]
        emails_bd_today.append(email_bd_today)
        print(email_bd_today)
# print(emails_bd_today)
# for i in emails_bd_today:
#     print(i)

#=====================

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "dibo.6606@gmail.com"
password = input("Type your password and press enter: ")
#receiver_email = "66dibo@gmail.com"
message = """\
Subject: Hi there
Polu4i li emaila

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() # ????Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # ????Can be omitted
    server.login(sender_email, password)
    print('Login successful')
    # TODO: Send email here
#==================

    for i in range(len(emails_bd_today)):
        receiver_email = emails_bd_today[i]

#================
        server.sendmail(sender_email, receiver_email, message)
        print(f"Send mail to :{receiver_email}")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
    print("Successfully sent email")

#===============================================
# email = 'dibo.6606@gmail.com' # Your email
# password = input(str("Enter your pass: ")) # Your email account password
# send_to_email = '66dibo@gmail.com' # Who you are sending the message to
# message = 'This is my message Hiiiiiiiiiiiiiii' # The message in the email
#
# server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
# server.starttls() # Use TLS
# server.login(email, password) # Login to the email server
# server.sendmail(email, send_to_email , message) # Send the email
# server.quit() # Logout of the email server
#=============================================