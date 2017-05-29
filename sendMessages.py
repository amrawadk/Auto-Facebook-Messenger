# This script sends messages to people with 'Pending' status in
# the messages table.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import webHandler
import sqlite3
import time

def ChangeLanguage():
    pyautogui.keyDown('altright')
    pyautogui.press('shiftright')
    pyautogui.keyUp('altright')

def TypeMessage(msgBody):
    ChangeLanguage()
    pyautogui.typewrite(msgBody)
    ChangeLanguage()

# Connect to SQL Database
connection = sqlite3.connect('FB_Friends.db')
cursor = connection.cursor()

# Open a new window in Google Chrome
driver = webdriver.Chrome()

# Login to Facebook Account
webHandler.LoginToFacebook(driver)

# Get relevant coloumns from 'Messages' Table
cursor.execute("SELECT MessangerLink, Message, MappedMessage, Status, Name \
    FROM Messages WHERE Status = 'Pending'")

for row in cursor.fetchall():
    # Open a messanger window
    webHandler.OpenAccount(driver, row[0])
    # Type message in window (Chrome window must be active)
    TypeMessage(row[2])
    # Press send
    #pyautogui.press('enter')
    
    # Change Status to 'Sent'
    cursor.execute('UPDATE Messages SET Status = "Sent" \
        WHERE MessangerLink = ?',(row[0],))
    connection.commit()

    print('Message sent to ',row[4])
