import sqlite3

conn = sqlite3.connect('Flights.db' )
c = conn.cursor()


c.execute("INSERT INTO flight (origin, destination, duration) VALUES ('Alger','Paris', 120 )")
c.execute("INSERT INTO flight (origin, destination, duration) VALUES ('Jijel','Alger', 45 )")

c.execute('SELECT * FROM flight WHERE duration < 60')
print(c.fetchall())
conn.commit()
conn.close()