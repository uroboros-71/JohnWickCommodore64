import os
import sqlite3
from abc import ABCMeta

class InitDatabase(metaclass=ABCMeta):
    def add_member(self, contact):
        self._db.cursor().execute('''
            INSERT INTO member(membercode, name, phone, bankname, bankaccount, notes, status)
            VALUES(:membercode, :name, :phone, :address, :email, :notes, :status)''',
                                  contact)
        self._db.commit()

    def get_member_summary(self):
        return self._db.cursor().execute(
            '''SELECT (name || SUBSTR("                                    ", 0, 27-LENGTH(name))) || status, id FROM member''').fetchall()

    def get_member(self, contact_id):
        return self._db.cursor().execute(
            "SELECT * FROM member WHERE id=:id", {"id": contact_id}).fetchone()

    def get_current_member(self):
        if self.current_id is None:
            return {"membercode": "","name": "", "bankname": "", "phone": "", "bankaccount": "", "notes": "", "status": ""}
        else:
            return self.get_member(self.current_id)

    def update_current_member(self, details):
        if self.current_id is None:
            self.add_member(details)
        else:
            self._db.cursor().execute('''
                UPDATE member SET name=:name, phone=:phone, bankname=:bankname,
                bankaccount=:bankaccount, notes=:notes, status=:status WHERE id=:id''',
                                      details)
            self._db.commit()

    def get_transmit_data(self):
        return self._db.cursor().execute(
            '''SELECT ("]SENDING MESSAGE TO...." || phone) || "\n" AS msg FROM member WHERE status LIKE "%ALIVE%"''').fetchall()

    def get_transmit_data_orderby(self):
        return self._db.cursor().execute(
            '''SELECT ("]SENDING MESSAGE TO...." || phone) || "\n" AS msg FROM member WHERE status LIKE "%ALIVE%" ORDER BY membercode''').fetchall()

    def add_account(self, contact):
        self._db.cursor().execute('''
            INSERT INTO account(accountnumber, name, bounty, distribution, status, lastseen, contractupd, authorization)
            VALUES(:accountnumber, :name, :bounty, :distribution, :status, :lastseen, :contractupd, :authorization)''',
            contact)
        self._db.commit()

    def get_account_summary(self):
        return self._db.cursor().execute(
            '''SELECT (((name || SUBSTR("                            ", 0, 15-(LENGTH(name)))) || "" || bounty) || SUBSTR("                            ", 0, 18-(LENGTH(bounty)))) || status, id FROM account''').fetchall()

    def get_account(self, contact_id):
        return self._db.cursor().execute(
            "SELECT * FROM account WHERE id=:id", {"id": contact_id}).fetchone()

    def get_current_account(self):
        if self.current_id is None:
            return {"accountnumber": "", "name": "", "bounty": "", "distribution": "", "status": "", "lastseen": "", "contractupd": "", "authorization": ""}
        else:
            return self.get_account(self.current_id)

    def get_max_id(self):
        return self._db.cursor().execute(
            '''SELECT MAX(id) AS id FROM account''').fetchone()

    def delete_account(self, contact_id):
        self._db.cursor().execute("DELETE FROM account WHERE id=:id", {"id": contact_id})
        self._db.commit()

    def update_current_account(self, details):
        if self.current_id is None:
            self.add_account(details)
        else:
            self._db.cursor().execute('''
                UPDATE account SET name=:name, bounty=:bounty, distribution=:distribution,
                status=:status, lastseen=:lastseen, contractupd=:contractupd WHERE id=:id''',
                details)
            self._db.commit()

    def create_table(self):
        # Create the basic contact table.
        # self._db.cursor().execute("DROP TABLE IF EXISTS member")
        self._db.cursor().execute('''
            CREATE TABLE IF NOT EXISTS member(
                id INTEGER PRIMARY KEY,
                membercode TEXT UNIQUE,
                name TEXT,
                phone TEXT,
                bankname TEXT,
                bankaccount TEXT,
                notes TEXT,
                status TEXT)
        ''')
        self._db.commit()

        # self._db.cursor().execute("DROP TABLE IF EXISTS account")
        self._db.cursor().execute('''
            CREATE TABLE IF NOT EXISTS account(
                id INTEGER PRIMARY KEY,
                accountnumber TEXT,
                name TEXT,
                bounty TEXT,
                distribution TEXT,
                status TEXT,
                lastseen TEXT,
                contractupd TEXT,
                authorization TEXT)
       ''')
        self._db.commit()

    def insert_member_data(self):
        cur = self._db.cursor()
        data = [("LN 02-0714", "John, Wick", "916-085-2930", "JN Cayman", "5186259017", "", "EXCOMUNICAD"),
                ("LN 02-0702", "Marcus", "315-194-6020", "ING Luxembourg bank", "8602930292", "", "DECEASED"),
                ("LN 02-0694", "Ares", "646-061-4988", "NCB Cayman Limited", "7194217400", "", "DECEASED"),
                ("LN 02-0743", "Cassian", "+39-12-4156-6020", "Banque de Luxembourg", "8572733103", "", "DECEASED"),
                ("LN 02-0734", "Zero", "917-139-5263", "Bank Julius Bär & Co. AG", "9197678175", "", "DECEASED"),
                ("LN 02-0812", "Ms. Perkins", "646-115-7259", "Barclays Bank Delaware", "3105499319", "", "DECEASED"),
                ("LN 02-0888", "Mr. Nobody", "315-078-6497", "WSFS Bank", "7703598588", "", "ALIVE"),
                ("LN 02-0612", "Tick-Tock Man", "214-378-2890", "Artisans' Bank", "6266729887", "", "ALIVE"),
                ("LN 07-0120", "Shimazu Koji", "+81-30-2385-2957", "LOMBARD ODIER", "03034899898", "", "ALIVE"),
                ("LN 02-0720", "Sofia Al-Azwar", "212-142-8538", "Bank Julius Bär & Co. AG", "9161766345", "", "ALIVE"),
                ("LN 07-0411", "Shimazu Akira", "+81-90-6238-5887", "LOMBARD ODIER", "08081762344", "", "ALIVE"),
                ("LN 03-0505", "Caine", "+33-15-077-2231", "Pictet", "Bank J. Safra Sarasin", "2277968493", "ALIVE"),
                ("LN 02-0700", "The Bowery King", "012-302-3344", "The Delaware National Bank", "8972432551", "", "ALIVE"),
                ("LN 02-0521", "The Doctor", "315-077-2231", "Applied Bank", "7592069814", "", "ALIVE"),
                ("LN 02-0330", "Winston Scott", "917-090-1143", "LOMBARD ODIER", "3145069814", "", "ALIVE"),
                ("LN 02-0639", "Ernest", "917-336-0909", "", "", "", "DECEASED"),
                ("LN 02-0654", "Viggo Tarasov", "213-997-5439", "", "", "", "DECEASED"),
                ("LN 02-0655", "Abram Tarasov", "214-678-9430", "", "", "", "ALIVE"),
                ("LN 02-0555", "Vincent Bisset de Gramont", "+33-55-958-7185", "", "", "", "ALIVE"),
                ("LN 02-0451", "The Harbinger", "+1-212-156-9932", "", "+1-212-156-9932", "", "ALIVE"),
                ("LN 02-0509", "The Director", "+81-97-8077-6590", "", "", "", "ALIVE"),
                ("LN 02-0567", "Julius", "+39-45-4791-0001", "", "", "", "ALIVE"),
                ("LN 02-0832", "The Shinobi", "219-409-4545", "", "", "", "ALIVE"),
                ("LN 02-0823", "Violin Assassin", "310-501-4698", "", "", "", "ALIVE"),
                ("LN 02-0801", "Killa Harkan", "+49-20-7946-0999", "Cayman Islands Development Bank", "1374855635", "", "ALIVE")]
        cur.executemany(
            "INSERT INTO member(membercode, name, phone, bankname, bankaccount, notes, status) VALUES (?,?,?,?,?,?,?)", data)
        self._db.commit()

    def insert_account_data(self):
        cur = self._db.cursor()
        data = [("9305-05",
                "John, Wick",
                "$7 MILLION USD",
                "WOLDWIDE",
                "CLOSED",
                "LINCOLN CENTER",
                "CONTRACT CLOSED",
                "Santino D'Antonio"),
                # ("1111-11",
                # "John, Wick",
                # "$14 MILLION USD",
                # "WOLDWIDE",
                # "PENDING",
                # "CENTRAL PARK",
                # "6:00 PM\nEXCOMMUNICAD",
                # "Winston Scott"),
                ("8908-03",
                "ROCKMAN L",
                "$2 MILLION USD",
                "WOLDWIDE",
                "OPEN",
                "HARKEM 4202",
                "ACTIVE",
                "Vincent Bisset de Gramont"),
                ("9401-21",
                "VASILYYEN M",
                "$375K USD",
                "WOLDWIDE",
                "CLOSED",
                "FORDHAM 4141",
                "",
                "Gianna D'Antonio"),
                ("6555-04",
                "BLUMENBERG K",
                "$350K USD",
                "WOLDWIDE",
                "OPEN",
                "STUYVESANT 0717",
                "",
                "Killa Harkan"),
                ("8989-21",
                "ZAYUSEV G",
                "$7 MILLION USD",
                "WOLDWIDE",
                "OPEN",
                "FINANCIAL",
                "",
                "The Elder")

        ]
        cur.executemany(
            "INSERT INTO account(accountnumber, name, bounty, distribution, status, lastseen, contractupd, authorization) VALUES (?,?,?,?,?,?,?,?)", data)
        self._db.commit()


class ContinentalModel(InitDatabase):
    def __init__(self):
        # Create a database in FILE.
        self._db = sqlite3.connect('continental.db')
        self._db.row_factory = sqlite3.Row

        if not os.path.isfile('continental.db'):
            # Create table.
            self.create_table()

            # Insert Initial data
            self.insert_member_data()

            # Insert Initial data
            self.insert_account_data()

        # Current contact when editing.
        self.current_id = None


class memoryContinentalModel(InitDatabase):
    def __init__(self):
        # Create a database in RAM.
        self._db = sqlite3.connect(':memory:')
        self._db.row_factory = sqlite3.Row

        # Create table.
        self.create_table()

        # Insert Initial data
        self.insert_member_data()

        # Insert Initial data
        self.insert_account_data()

        # Current contact when editing.
        self.current_id = None


