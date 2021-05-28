import sqlite3
#conn = sqlite3.connect('customer.db')#creating and connecting to db
#conn = sqlite3.connect(':memory')# connecting to an existing database
#c = conn.cursor() # create the cursor
#create a table
# c.execute("""CREATE TABLE customers(
#     first_name text,
#     last_name text,
#     email text
#     )""")
# conn.commit() #commit our command
# conn.close()# closing the connection

#Insert into table
# c = conn.cursor()
# c.execute("INSERT INTO customers VALUES ('John','Elder','john@yahoo.com')")
# conn.commit() #commit our command
# conn.close()# closing the connection

# conn = sqlite3.connect('customer.db')
# c = conn.cursor()
# c.execute("INSERT INTO customers VALUES ('Tim','Smith','tim@yahoo.com')")
# conn.commit() #commit our command
# conn.close()# closing the connection

# conn = sqlite3.connect('customer.db')
# c = conn.cursor()
# c.execute("INSERT INTO customers VALUES ('Mary','Beth','mary@yahoo.com')")
# conn.commit() #commit our command
# conn.close()# closing the connection

# conn = sqlite3.connect('customer.db')
# c = conn.cursor()
# many_customers = [
#                 ('Wes','Brown','wes@brown.com'),
#                 ('Stef', 'King','stef@gmail.com'),
#                 ('Dan','Childs','dan@yahoo.com'),
#                 ]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
# conn.commit() #commit our command
# conn.close()# closing the connection

#Query the database
#c = conn.cursor()
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
# c.fetchone()
# c.fetchmany(3)
#UPDATE Records
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 1")
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")
#c.execute("DROP TABLE customers ")
# print(c.fetchall())
# conn.commit() #commit our command
# conn.close()

# Query the DB and return All Records
def show_all():
    #connect to db
    conn = sqlite3.connect('customer.db')
    #create the cursor
    c = conn.cursor()

    #query the db
    c.execute("SELECT rowid,* FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)
    conn.commit()  #commit our command
    conn.close()  # close our connection

#add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES(?,?,?)", (first,last,email))
    conn.commit()
    conn.close()

#del a  record to the table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)",id)
    conn.commit()
    conn.close()