from pandas as pd
import sqlite3
import openpyxl
file2_PD = pd.read_excel("~/PycharmProgects/terminals.xlsx")
file_PD = pd.read_csv("~/PycharmProjects/transactions.txt")
connection = sqlite3.connect("Database.db")
cursor = connection.cursor()
cursor.execute('''DROP TABLE Tabl2
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
    transaction_id BIGINTEGER,
    transaction_date DATETIME,
    amount FLOAT,
    card_num INTEGER,
    oper_type TEXT,
    oper_result TEXT,
    terminal TEXT,
    foreign key (terminal) REFERENCES Tabl2 (terminal_id)
    )
''')
# cursor.execute('''DROP TABLE User
# ''')
i=0
a=len(file_PD)
while i < a:
    m = []
    for b in file_PD.iloc[i]:
        m.append(b)
    cursor.execute("INSERT INTO User (transaction_id, transaction_date, amount, card_num, oper_type, oper_result, terminal) VALUES (?, ?, ?, ?, ?, ?, ?);",  (m[0], m[1], m[2], m[3], m[4], m[5], m[6]))
    connection.commit()
    i += 1
    connection.close()
