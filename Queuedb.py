import sqlite3

con = sqlite3.connect("queue.db")
print("Database opened successfully")

con.execute(
    "create table Queues (Datet TEXT DEFAULT CURRENT_TIMESTAMP,Ambid INTEGER PRIMARY KEY AUTOINCREMENT , Queueid INTEGER NOT NULL, Amount INTEGER NOT NULL,Taskcount INTEGER NOT NULL,State TEXT NOT NULL,Reason TEXT NOT NULL)")

print("Table created successfully")

con.close()