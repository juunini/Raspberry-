import psycopg2 as db

conn = db.connect("host=localhost dbname=dht11 user=postgres password=1234")
cur = conn.cursor()

cur.execute("""
    SELECT column_name
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'dht11'
""")
describe = cur.fetchall()

for desc in describe :
    print(desc[0], end = '\t\t')
    
print('\n----------------------------------------------------------------')

cur.execute("SELECT * FROM dht11")
rows = cur.fetchall()

for row in rows :
    for r in row :
        print(r, end = '\t')
    print()

cur.close()
conn.close()
