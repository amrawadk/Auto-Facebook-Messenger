# This script is used to update the friends database

import fbchat
import sqlite3

username = input('Facebook email: ')
password = input('Facebook password: ')

# Login to facebook
client = fbchat.Client(username, password)

# Connect to SQL Database
connection = sqlite3.connect('FB_Friends.db')
cursor = connection.cursor()

def getUsers(client, Relation, Gender, Category, Adj):
    while True:
        friends = client.getUsers(input('Name to find:'))
        for friend in friends:
            print(friend)
            reply = input('Add to list ?')
            if reply == 'y':
                NickName = input('NickName: ')
                cursor.execute('INSERT INTO friends values(?,?,?,?,?,?,?,?)',\
                    (Relation, Category, friend.name, friend.url, friend.uid, NickName,
                     Gender, Adj))
                connection.commit()
            elif reply == 'q':
                return
            else:
                print('Discarded!')
    
# Fill in Table
while True:
    Gender = input('Gender:')
    Category = input('Category: ')
    Adj = input('Adj: ')
    Relation = input('Relation: ')
    print(Gender, Category, Adj, Relation)
    getUsers(client, Relation, Gender, Category, Adj)
