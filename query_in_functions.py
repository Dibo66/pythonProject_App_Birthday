import sqlite3


def read_Sqlite_Table():
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from addressbook"""
        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        return records
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Surname: ", row[2])
            print("EMAIL: ", row[3])
            print("Phone: ", row[4])
            print("Birthdate: ", row[6])
            print("Address: ", row[5])
            print("\n")

        cur.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

def get_person_Info(person_id):
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        print("Connected to SQLite")

        sql_select_query = """SELECT * FROM addressbook WHERE person_id = ?"""
        cur.execute(sql_select_query, (person_id,))
        records = cur.fetchall()
        print(records)
        print("Printing ID ", person_id)
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Surname: ", row[2])
            print("EMAIL: ", row[3])
            print("Phone: ", row[4])
            print("Birthdate: ", row[6])
            print("Address: ", row[5])
            print("\n")
        cur.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")

def read_person_Id(personId):
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from addressbook where person_id = ?"""
        cur.execute(sqlite_select_query, (personId,))
        print("Reading single row \n")
        row = cur.fetchone()
        print(row)
        print("Id: ", row[0])
        print("Name: ", row[1])
        print("Surname: ", row[2])
        print("EMAIL: ", row[3])
        print("Phone: ", row[4])
        print("Birthdate: ", row[6])
        print("Address: ", row[5])
        print("\n")
        return row
        cur.close()

    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def insert_person(name, surname, email, phone, address, birthdate):
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO addressbook
                          (person_name, person_surname, person_email, person_phone, person_address, person_birthdate) 
                          VALUES (?, ?, ?, ?, ?, ?);"""

        data_tuple = (name, surname, email, phone, address, birthdate)
        cur.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into addressbook table")

        cur.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def update_Sqlite_Table(name, surname, email, phone, address, birthdate, id):
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        print("Connected to SQLite")

        sql_update_query = """UPDATE addressbook SET person_name = ?, person_surname = ?, person_email = ?, person_phone = ?, person_address = ?, person_birthdate = ? 
                    WHERE person_id = ?"""
        data = (name, surname, email, phone, address, birthdate, id)
        cur.execute(sql_update_query, data)
        conn.commit()
        print("Record Updated successfully")
        cur.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The sqlite connection is closed")

def bday_persons():
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * FROM addressbook WHERE SUBSTR(person_birthdate, 6) = SUBSTR((SELECT date('now','localtime')), 6);"""
        cur.execute(sqlite_select_query)
        records = cur.fetchall()

        print("Total rows are:  ", len(records))
        print("Printing row: ")
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Surname: ", row[2])
            print("EMAIL: ", row[3])
            print("Phone: ", row[4])
            print("Birthdate: ", row[6])
            print("Address: ", row[5])
            print("\n")

        return records
        cur.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


def delete_Sqlite_Record(personId):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from addressbook where person_id = ?"""
        cursor.execute(sql_update_query, (personId, ))
        conn.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("sqlite connection is closed")

