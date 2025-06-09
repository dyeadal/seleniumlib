# Created by dyeadal
# GNU General Public License 3.0

from selenium.webdriver.common.by import By # Allows searching for HTML tags
from selenium.webdriver.common.keys import Keys # Allows keyboard emulation
import time # Used to sleep/standby
import random # Used to create random sleep/standby

import undetected_chromedriver as ucd

# Start the session using undetected chromedriver
driver = ucd.Chrome()

# Wait for X seconds
def Wait(seconds):
    print(f"Waiting for {seconds} seconds...")
    time.sleep(seconds)

# Wait for 1 to 10 seconds randomly
def RandomWait():
    num = random.randint(1, 10)
    print(f"Waiting randomly for {num} seconds...")
    time.sleep(num)

# Close browser
def CloseBrowser():
    print("Closing browser!")
    driver.quit()

# Open URL
def OpenPage(url):
    print(f"Opening {url}")
    driver.get(url)

# Find element on webpage by its class name
def FindElementByClass(classname):
    print(f"Finding element by class {classname}")
    element = driver.find_element(By.CLASS_NAME, classname)
    return element

# Click on an Element
def ClickElement(element):
    print(f"Clicking element {element}")
    object = driver.find_element_by_name({element})
    object.click()

# Emulate scrolling on an element
def ScrollElement(element):
    print(f"Scrolling element {element}")
    # Yet to implement

# Insert text directly and fast
def InsertText(element, text):
    element.send_keys(text)

# Insert text as if it were being typed out by a human
def TypeTextInClass(elementClassName, text):

    # Find element by class name and store as variable
    element = FindElementByClass(elementClassName)

    # Store list of keys and time took to "type" each key
    seclist = "Pressed keys:"

    # Loop through each character in the string
    for item in text:
        # Send single character to element
        element.send_keys(item)
        # Create random float variable num
        num = random.random()
        # Add imitated key pressed and the seconds it took to list
        seclist = seclist + (f"{item} : {num}, ")
        # Wait for random number of milliseconds
        time.sleep(num)

    print(f"Imitated a human typing on a keyboard:\n{seclist}\n")

# Press Enter key on an Element
def PressEnter(elementClassName):
    # Find element by class name and store as variable
    element = FindElementByClass(elementClassName)
    print(f"Pressing Enter Key in {element}")
    # Send ENTER key on element
    element.send_keys(Keys.ENTER)
