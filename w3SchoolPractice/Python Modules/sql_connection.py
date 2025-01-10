import sqlite3

print("creating connecting")

conn = sqlite3.connect("mydatabase.db")
conn.close()

print("The sqlite connection is closed")