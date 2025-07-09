import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='YOUR_USER_HERE' password='YOUR_PASSWORD_HERE' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    cur.close()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='YOUR_USER_HERE' password='YOUR_PASSWORD_HERE' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')")
    conn.commit()
    cur.close()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='YOUR_USER_HERE' password='YOUR_PASSWORD_HERE' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='YOUR_USER_HERE' password='YOUR_PASSWORD_HERE' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='database1' user='YOUR_USER_HERE' password='YOUR_PASSWORD_HERE' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


# Crear la tabla antes de insertar datos
create_table()
insert("Orange",10,15)
# delete("Watter Glass")
# update(11, 6, "Water Glass")
# print(view())
