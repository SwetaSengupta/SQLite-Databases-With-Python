import sqlite3
conn = sqlite3.connect('customer.db')#creating and connecting to db
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
c = conn.cursor()
c.execute("INSERT INTO customers VALUES ('John','Elder','john@yahoo.com')")
conn.commit() #commit our command
conn.close()# closing the connection

conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute("INSERT INTO customers VALUES ('Tim','Smith','tim@yahoo.com')")
conn.commit() #commit our command
conn.close()# closing the connection

conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute("INSERT INTO customers VALUES ('Mary','Beth','mary@yahoo.com')")
conn.commit() #commit our command
conn.close()# closing the connection


