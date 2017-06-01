# This script is used to update the friends database

import fbchat
import sqlite3

username = str('Facebook email: ')
password = input('Facebook password: ')

# Login to facebook
client = fbchat.Client(username, password)

# Connect to SQL Database
connection = sqlite3.connect('FB_Friends.db')
cursor = connection.cursor()

# Read Messages
cursor.execute("SELECT * FROM Messages")

for row in cursor.fetchall():
    sent = client.send(row[1], row[2])
    if sent:
        print("Message sent successfully to ", row[0])
        cursor.execute('UPDATE Messages SET Status = "Sent" \
            WHERE Name = ?',(row[0],))
        connection.commit()
