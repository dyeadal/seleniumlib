# Created by dyeadal
# GNU General Public License 3.0

from selenium.webdriver.common.by import By # Allows searching for HTML tags
from selenium.webdriver.common.keys import Keys # Allows keyboard emulation
import time # Used to sleep/standby
import datetime # Used to create logs and screenshots
import os # Used for log creation
import random # Used to create random sleep/standby
import undetected_chromedriver as ucd # Undetected chromedriver to avoid bot detection

SeleniumLibVersion = 0.1
LogEnable=False
LogLocation=None

# Start the session using undetected chromedriver
driver = ucd.Chrome()

##########################################################################
### Browser Actions
##########################################################################

# Open URL
def OpenPage(url):
    PrintAndLog(f"Opening {url}")
    driver.get(url)

# Close browser
def CloseBrowser():
    PrintAndLog("Closing browser.")
    driver.quit()

##########################################################################
### Human Emulation
##########################################################################

# Wait for X seconds, 2 by default
def Wait(seconds=2):
    PrintAndLog(f"Waiting for {seconds} seconds...")
    time.sleep(seconds)

# Wait for 1 to 10 seconds randomly by default, can be changed
def RandomWait(min=1, max=10):
    num = random.randint(min, max)
    PrintAndLog(f"Waiting randomly for {num} seconds...")
    time.sleep(num)

# Wait for random time. default between 0.1 and 2.0 seconds
def EmulateHumanHesitation(min=0.1, max=2.0):
    time.sleep(random.uniform(min, max))

# Insert text as if it were being typed out by a human
def TypeTextInClass(element, text):

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
    PrintAndLog(f"Imitated a human typing on a keyboard:\n{seclist}\n")

##########################################################################
### Keyboard Emulation
##########################################################################

# Press Enter key on an element
def PressEnter(element):
    PrintAndLog(f"Pressing Enter Key in {element}")
    # Send ENTER key on element
    element.send_keys(Keys.ENTER)

# Press Scroll Down key on an element
def ScrollDownButton(element):
    PrintAndLog(f"Scrolling down on {element}")
    element = FindElementByClass(element)
    element.send_keys(Keys.PAGE_DOWN)

# Insert text directly and fast
def InsertText(element, text):
    PrintAndLog(f"Inserting {text} into {element}")
    element.send_keys(text)

##########################################################################
### Mouse Emulation
##########################################################################

# Emulate scrolling to an element to be viewable on screen
def ScrollToElement(element):
    PrintAndLog(f"Scrolling to element")
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

# Click on an element based on Class
def ClickOnElement(element):
    print(f"Clicking element {element.text}")
    element.click()


##########################################################################
### Page Scraping
##########################################################################

# Find element on webpage by its class name
def FindElementByClass(classname):
    PrintAndLog(f"Finding element by class {classname}")
    element = driver.find_element(By.CLASS_NAME, classname)
    return element

# Find element on webpage by its ID name
def FindElementByID(idname):
    PrintAndLog(f"Finding element by ID name {idname}")
    element = driver.find_element(By.ID, idname)
    return element

# Find element using any By value for advance users (By.XPATH, By.CSS_SELECTOR, etc.)
def FindElement(by, value):
    PrintAndLog(f"Finding element by {by} {value}")
    element = driver.find_element(by, value)
    return element

# Return text contained in an element
def TextInElement(element):
    PrintAndLog(f"Returning text in element: {element}")
    return element.text

##########################################################################
### Debug and Logging
##########################################################################

def CurrentTime():
    raw_time = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    return raw_time

def FormattedCurrentTime():
    formatted_time = str(datetime.datetime.now().strftime("%m%d%Y_%H%M%S"))
    return formatted_time

# Enable logging, changing global variable. Functions will log actions
def EnableLogging():
    global LogEnable
    LogEnable = True

# Create Log File, default to user home directory and name prefix of "SeleniumLib"
def CreateLogFile(Directory=os.path.expanduser("~"), NamePrefix="SeleniumLib"):

    # Create the filename
    filename = f"{NamePrefix}_{FormattedCurrentTime()}.txt"

    # Create the path of where it is going to be created
    if LogLocation is None:
        filepath = os.path.join(Directory, filename)
    # Custom log filepath
    else:
        filepath = os.path.join(LogLocation, filename)

    # Try creating the file
    try:
        with open(filepath, "w") as file:
            file.write(f"Log created at {FormattedCurrentTime()}"
                       f"SeleniumLib version: {SeleniumLibVersion}"
                       f"Created by @dyeadal on GitHub"
                       f"Not liable for any damages caused by this script, please use responsibly")
            PrintAndLog(f"Log created at {FormattedCurrentTime()}", filepath)
            global LogLocation
            return LogLocation
    # If it fails print out message to terminal and ask if they want to quit or continue without logs
    except Exception as error:
        print(f"Failed to create {filename} log file.\nError: {error}")

# Create screenshot
def Screenshot(NamePrefix="SeleniumLibScreenshot"):
    name = f"{NamePrefix}_{FormattedCurrentTime()}.png"
    driver.save_screenshot(name)
    return name

# Function to print and write to log if variables are configured
def PrintAndLog(Message):

    print(Message)

    if LogEnable is True and LogLocation is not None:
        WriteToLog(LogLocation, Message)

    elif LogEnable is False and LogLocation is not None:
        print(f"LogLocation is configured to {LogLocation}, but logs are not enabled."
              f"Enable Logging by running the function 'EnableLogging()' in your script."
              f"Exiting script in 15 seconds...")
        Wait(15)
        exit()

    else:
        print(f"Logging is enabled, but no log file is configured. "
              f"Please change LogLocation variable from None to a custom location."
              f"Exiting in 15 seconds...")
        Wait(15)
        exit()

# Function to write to log
def WriteToLog(file, msg):

    if LogEnable is True and LogLocation is not None:
        try:
            with open(file, 'a') as file:
                file.write(CurrentTime() + " --- " + msg + "\n")
        except Exception as e:
            print(f"An error occurred writing to file: {e}")
    elif LogEnable is False and LogLocation is not None:
        print(f"LogLocation is configured to {LogLocation}, but logs are not enabled."
              f"Enable Logging by running the function 'EnableLogging()' in your script."
              f"Exiting script in 15 seconds...")
        Wait(15)
        exit()

    else:
        print(f"Logging is enabled, but no log file is configured. "
              f"Please change LogLocation variable from None to a custom location."
              f"Exiting in 15 seconds...")
        Wait(15)
        exit()
