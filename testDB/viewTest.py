import psycopg2 as db

conn = db.connect("host=localhost dbname=dht11 user=postgres password=1234")
cur = conn.cursor()

# postgreSQL에는 describe기능이 없어서 이렇게 읽어와야 함
cur.execute("""
    SELECT column_name
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'dht11'
""")
describe = cur.fetchall()

# date \t\t time \t\t temperature \t\t humidity
for desc in describe :
    print(desc[0], end = '\t\t')

# 절취선
print('\n----------------------------------------------------------------')

# 테이블에서 데이터를 읽어옴
cur.execute("SELECT * FROM dht11")
rows = cur.fetchall()

for row in rows :
    for r in row :
        print(r, end = '\t')
        if row[len(row) - 2] == r :
            print('\t\t', end = '')
    print()

# 접속종료
cur.close()
conn.close()
