import sqlite3 as sq

con = sq.connect("saper.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL
            )""")

# cur.execute("""INSERT INTO users (name, city)
#             VALUES ('Sasha', 'Moscow'), ('Kolya', 'Saints-Peterburg')
#             """)

cur.execute("SELECT * FROM users")
result = cur.fetchall()
# for row in cur.fetchall():
#     print(row)
print(type(result))
for row in result:
    print(row)

con.commit()
con.close()