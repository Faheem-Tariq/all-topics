import sqlite3

# Connect to the database
conn = sqlite3.connect("fast_food_orders.db")

# Create a cursor
cursor = conn.cursor()

# Create a table for orders
cursor.execute("""CREATE TABLE IF NOT EXISTS orders (item text, price real)""")

# Insert the order information
cursor.execute("""INSERT INTO orders VALUES (?, ?)""", (item_name, item_price))

# Commit the changes and close the connection
conn.commit()
conn.close()
