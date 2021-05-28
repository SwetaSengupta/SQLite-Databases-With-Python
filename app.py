from db import show_all
import db
#db.delete_one('8') # del record row id
#db.add_one("Laura","Smith","laura@smith.com") #add a record
#add many records
stuff = [
    ('Brenda', 'Smith', 'brenda@smith.com'),
    ('Joshua','Raintree','joshua@raintree.com')
    ]
db.add_many(stuff)
db.show_all()