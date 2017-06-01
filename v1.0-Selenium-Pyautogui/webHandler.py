# This script contains common browser functions for 'sendMessages' script.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

def LoginToFacebook(driver):
    # Log in to facebook account
    email = input('Facebook Email: ')
    password = input('Facebook Password: ')

    driver.get("http://www.facebook.org")
    assert "Facebook" in driver.title
    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys(email)
    elem = driver.find_element_by_name("pass")
    elem.clear()
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    # todo: Check if login is successful
    
    # Remove save password popup
    pyautogui.press('esc')
    
def OpenAccount(driver, AccountLink):
    driver.get(AccountLink)
    # Remove any popups
    pyautogui.press('esc')
