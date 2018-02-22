import psycopg2 as db

conn = db.connect("host=localhost dbname=dht11 user=postgres password=1234")
cur = conn.cursor()

cur.execute("SELECT * FROM dht11")
rows = cur.fetchall()

print("date\t\t\ttemperature\thumidity")
for row in rows:
    print("{}\t{}\t\t{}".format(row[0], row[1], row[2]))

cur.close()
conn.close()
