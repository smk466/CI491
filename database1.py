from tkinter import *
from PIL import ImageTk,Image
import sqlite3

# Create a database
conn = sqlite3.connect('newdatabase.db')

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE database (
		search text,
		name text,
		email text
		)""")





# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()