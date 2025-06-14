# Created by dyeadal
# GNU General Public License 3.0
from xml.etree.ElementPath import xpath_tokenizer

SeleniumLibVersion = 0.1

from selenium.webdriver.common.by import By # Allows searching for HTML tags
from selenium.webdriver.common.keys import Keys # Allows keyboard emulation
from selenium.webdriver.support.wait import WebDriverWait # used to wait on loading pages
from selenium.webdriver.support import expected_conditions # used to find and confirm page content loaded

import time # Used to sleep/standby
import datetime # Used to create logs and screenshots
import os # Used for log creation
import random # Used to create random sleep/standby
import undetected_chromedriver as ucd # Undetected chromedriver to avoid bot detection

LogEnable = False # enable or disable logging to a text file
LogLocation = None # set custom log location
TimeoutSecToLoad = 30 # set seconds before timeout

# Start the session using undetected chromedriver
driver = ucd.Chrome()

##########################################################################
### Browser Actions
##########################################################################

# Open URL
def OpenPage(url):

    i = input(f"You are attempting to access:\n\n {url}.\n\n Would you like to continue? [Y/n] ")

    # User confirms URL is correct and wants to proceed with accessing website
    if i == "Y" or i == "y":
        # Print and Log function use of OpenPage()
        PrintAndLog(f"Opening {url} via OpenPage() function.")
        # Perform HTTP GET of URL
        driver.get(url)

        # Wait to see page load
        try:
            # Wait until condition is met, timeouts after so many seconds set by TimeoutSecToLoad variable
            WebDriverWait(driver, TimeoutSecToLoad).until(
                # Condition = Until it can see the <body> tag to see page contents
                expected_conditions.presence_of_element_located((By.TAG_NAME, "body")) # takes only one argument, double enclosed ()s
            )
            PrintAndLog(f"URL successfully loaded, can see <body> tag.")
            # Wait for a moment before continuing
            EmulateHumanHesitation()

        # Fails to load in given time
        except Exception as error:
            ErrorHandler(f"URL failed to load in time, can't see <body> tag.\n Error: {error}")

    # Operator chooses no, likely due to URL being incorrect
    else:
        PrintAndLog(f"Operator decline to continue to access {url} via OpenPage() function.\n Closing browser.")
        CloseBrowser()

# Close browser
def CloseBrowser():
    PrintAndLog(f"Closing browser via CloseBrowser() function.")
    try:
        driver.quit()
        PrintAndLog("Closed browser.")
    except Exception as error:
        ErrorHandler(f"Failed to close browser.\nError: {error}")

##########################################################################
### Human Emulation
##########################################################################

# Wait for X seconds, 3 by default
def Wait(seconds=3):
    PrintAndLog(f"Waiting for {seconds} seconds via Wait() function.")
    try:
        time.sleep(seconds)
    except Exception as error:
        ErrorHandler(f"Failed to wait for {seconds} seconds.\nError: {error}")

# Wait for 3 to 10 seconds randomly by default, can be changed
def RandomWait(min=3, max=10):
    PrintAndLog(f"Attempting to randomly wait via RandomWait({min}, {max}) function.")
    try:
        num = random.randint(min, max)
        PrintAndLog(f"Waiting randomly for {num} seconds via RandomWait() function.")
        time.sleep(num)
    except Exception as error:
        ErrorHandler(f"Failed to wait for {num} seconds.\n Error: {error}")

# Wait for random time. default between 0.1 and 2.0 seconds
def EmulateHumanHesitation(min=3.0, max=7.0):
    PrintAndLog(f"Emulating human hesitation via EmulateHumanHesitation() function with values {min}, {max}.")
    try:
        time.sleep(random.uniform(min, max))
    except Exception as error:
        ErrorHandler(f"Emulating human hesitation failed.\n Error: {error}")

##########################################################################
### Keyboard Emulation
##########################################################################

# Insert text as if it were being typed out by a human
def TypeTextInElement(element, text):
    PrintAndLog(f"Emulating {text} via TypeTextInClass() function in element {element}.")
    # Store list of keys and time took to "type" each key
    seclist = "Pressed keys:"

    # Loop through each character in the string
    try:
        for item in text:
            # Create random float variable num
            num = random.random()

            # Wait for random number of milliseconds
            time.sleep(num)

            # Send single character to element
            element.send_keys(item)

            # Add imitated key pressed and the seconds it took to list
            seclist = seclist + (f"{item} : {round(num, 2)}, ")

        PrintAndLog(f"Successfully imitated a human typing on a keyboard:\n{seclist}\n")
    except Exception as error:
        ErrorHandler(f"Failed imitating typing {text} into element {element}.\n Error: {error}")

# Press Enter key on an element
def PressEnter(element):
    PrintAndLog(f"Pressing the enter key on element {element}.")
    try:
        # Send ENTER key on element
        element.send_keys(Keys.ENTER)
        PrintAndLog(f"Pressed Enter Key in {element}")
    except Exception as error:
        ErrorHandler(f"Failed pressing enter key in {element}.\n Error: {error}")

# Press Page Down key on an element
def PressPageDown(element):
    PrintAndLog(f"Pressing the page down key on element {element}.")
    try:
        element = FindElementByClass(element)
        element.send_keys(Keys.PAGE_DOWN)
        PrintAndLog(f"Scrolled down on {element}")
    except Exception as error:
        ErrorHandler(f"Failed scrolling down on {element}.\n Error: {error}")

# Press Page Up key on an element
def PressPageUp(element):
    PrintAndLog(f"Pressing the page up key on element {element}.")
    try:
        element = FindElementByClass(element)
        element.send_keys(Keys.PAGE_UP)
        PrintAndLog(f"Scrolled up on {element}")
    except Exception as error:
        ErrorHandler(f"Failed scrolling up on {element}.\n Error: {error}")

# Insert text directly and fast
def InsertText(element, text):
    PrintAndLog(f"Inserting {text} on element {element}.")
    try:
        element.send_keys(text)
        PrintAndLog(f"Inserted {text} into {element}")
    except Exception as error:
        ErrorHandler(f"Failed inserting {text} into {element}.\n Error: {error}")

##########################################################################
### Mouse Emulation
##########################################################################

# Emulate scrolling to an element to be viewable on screen
def ScrollToElement(element):
    PrintAndLog(f"Scrolling to element {element}.")
    # contain text in case element is stale
    txt = element.text
    try:
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        PrintAndLog(f"Scrolled to element containing {txt}")
    except Exception as error:
        ErrorHandler(f"\nFailed scrolling to element containing{txt}.\n Error: {error}")

# Click on an element based on Class
def ClickOnElement(element):
    PrintAndLog(f"Clicking on element {element}.")
    try:
        #Store elements text as a variable, stale elements caused issues identifying which element is throwing error
        txt = element.text
        # Scroll to element to avoid UI issue or errors
        ScrollToElement(element)
        # Stop and wait a moment
        EmulateHumanHesitation()
        # Click on element
        element.click()
        print(f"Clicked on element containing {txt}")
    except Exception as error:
        ErrorHandler(f"\nFailed clicking on element containing {txt}.\n Error: {error}")

##########################################################################
### Page Scraping
##########################################################################

# Find element on webpage by its class name
def FindElementByClass(classname):
    PrintAndLog(f"Finding element by class {classname}")
    #
    try:
        element = driver.find_element(By.CLASS_NAME, classname)
        PrintAndLog(f"Found element by class {classname}")
        return element
    #
    except Exception as error:
        ErrorHandler(f"Failed finding element by class {classname}.\n Error: {error}")
        return None

# Find element on webpage by its ID name
def FindElementByID(idname):
    PrintAndLog(f"Finding element by ID name {idname}")
    #
    try:
        element = driver.find_element(By.ID, idname)
        PrintAndLog(f"Found element by ID name {idname}")
        return element
    #
    except Exception as error:
        ErrorHandler(f"Failed finding element by ID name {idname}\n Error: {error}")
        return None

# Find the first element by tag and string
def FindElementByText(tag, string):
    PrintAndLog(f"Finding element by text name {string} in a {tag} tag.")
    # Try finding element using string

    # Common attributes that may contain the string the user is identifying in the element they are attempting to interact with
    common_attr = [
        'placeholder',
        'value',
        'alt',
        'title',
        'aria-label'
    ]

    try:
        # Build the XPath condition for all common attributes to search the string for
        attr_conds = " or ".join([
            f"contains(@{attr}, '{string}')" for attr in common_attr
        ])

        # Checks if element contain string or attributes that contain the string
        # normaliza-space removes white spaces to combat messy HTML
        xpath = f"//{tag}[contains(normalize-space(.), '{string}') or {attr_conds}]"
        return driver.find_element(By.XPATH, xpath)

    # If no element found with the text, throw error
    except Exception as error:
        ErrorHandler(f"Element with tag <{tag}> containing text '{string}' not found.\n Error: {error}.")
        return None

# Find ALL elements containing a string
# Useful when string and tag appears throughout your web page
# Stores results in a list to then be able to filter or interact with individually

def FindAllElementsByText(tag, string):
    PrintAndLog(f"Finding all elements by text name {string} in a {tag} tag.")
    try:
        xpath = f"//{tag}[.//text()[contains(., '{string}')]]"
        elements = driver.find_elements_by_xpath(xpath)
        return elements
    except Exception as error:
        ErrorHandler(f"Element tag {tag} with text '{string}' not found.\n Error: {error}")
        return None

# Find element using any By value for advanced users (By.XPATH, By.CSS_SELECTOR, etc.)
def FindElement(by, value):
    PrintAndLog(f"Finding element by {by} {value}")
    #
    try:
        element = driver.find_element(by, value)
        PrintAndLog(f"Found element by {by} {value}")
        return element
    #
    except Exception as error:
        ErrorHandler(f"Failed finding element by {by} {value}\n Error: {error}")
        return None

# Return text contained in an element
def ElementText(element):
    PrintAndLog(f"Returning text in element: {element.text}")
    #
    try:
        PrintAndLog(f"Returning text in element: {element.text}")
        return element.text
    #
    except Exception as error:
        ErrorHandler(f"Failed returning text in element {element}.\n Error: {error}")
        return None

# Compare a string to the text contained in an element
def IfTextInElement(string, element, casesensitive=True):
    PrintAndLog(f"Attempting to find string {string} in element {element}. Casesensitive: {casesensitive}.")
    # Case sensitivity enabled, runs this statement
    try:
        if casesensitive == True:
            # If found return true and log
            if string in element.text:
                PrintAndLog(f"The case sensitive string {string} was found in element: {element}.\n Returning True\nElement contains {element.text}")
                return True
            # If NOT found return false and log
            else:
                ThrowIntentionalError(f"The case sensitive string {string} was NOT found in element: {element}.\n Returning False\nElement contains {element.text}")
                return False
        # Case sensitivity disabled, runs this statement instead
        else:
            # If values using the lower() functions equals each other retunr true
            if str(string.lower()) in element.text.lower():
                PrintAndLog(f"The non-case sensitive string {string} was found in element: {element}.\n Returning True\nElement contains {element.text}")
                return True
            # If NOT found using lower()'ed strings return false and log
            else:
                ThrowIntentionalError(f"The non-case sensitive string {string} was NOT found in element: {element}.\n Returning False\nElement contains {element.text}")
                return False

    #
    except Exception as error:
        PrintAndLog(f"Failed to find string {string} in element {element}. Casesensitive: {casesensitive}.\n Error: {error}")
        return None

##########################################################################
### Debug and Logging
##########################################################################

#
def CurrentTime():
    PrintAndLog(f"Attempting to capture current time via CurrentTime() function.")
    #
    try:
        raw_time = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        PrintAndLog(f"Current time: {raw_time}")
        return raw_time
    #
    except Exception as error:
        ErrorHandler(f"Failed to capture current time via CurrentTime() function\n Error: {error}")
        return None

def FormattedCurrentTime():
    PrintAndLog(f"Attempting to format current time via FormattedCurrentTime() function.")
    #
    try:
        formatted_time = str(datetime.datetime.now().strftime("%m%d%Y_%H%M%S"))
        PrintAndLog(f"Successfully formatted current time: {formatted_time}")
        return formatted_time
    #
    except Exception as error:
        PrintAndLog(f"Failed to format current time via FormattedCurrentTime() function.\n Error: {error}")
        return None

# Enable logging, changing global variable. Functions will log actions
def EnableLogging():
    global LogEnable
    LogEnable = True

# Create Log File, default to user home directory and name prefix of "SeleniumLib"
def CreateLogFile(Directory=os.path.expanduser("~"), NamePrefix="SeleniumLib"):
    # Enable LogLocation to be Global
    global LogLocation

    # Create the filename
    filename = f"{NamePrefix}_{FormattedCurrentTime()}.txt"

    # Create the path of where it is going to be created
    if LogLocation is None:
        filepath = os.path.join(Directory, filename)
        LogLocation = filepath

    # Custom log filepath
    else:
        filepath = os.path.join(LogLocation, filename)
        LogLocation = filepath
    # Try creating the file
    try:
        with open(filepath, "w") as file:
            file.write(f"Log created at {FormattedCurrentTime()}\n"
                       f"SeleniumLib version: {SeleniumLibVersion}\n"
                       f"Created by @dyeadal on GitHub\n"
                       f"Not liable for any damages caused by this script, please use responsibly\n")
            print(f"Log file {filepath} created at {FormattedCurrentTime()}")
            return filepath
    # If it fails print out message to terminal and ask if they want to quit or continue without logs
    except Exception as error:
        print(f"Failed to create {filename} log file.\nError: {error}")
        return None

# Create screenshot
def Screenshot(NamePrefix="SeleniumLibScreenshot"):

    try: # taking a screenshot
        name = f"{NamePrefix}_{FormattedCurrentTime()}.png"
        driver.save_screenshot(name)
        return name

    # If error occurs
    except Exception as error:
          PrintAndLog(f"Failed to screenshot {name}.\nError: {error}")
          return None

# Function to print and write to log if variables are configured
def PrintAndLog(Message):
    global LogLocation

    # Default is to print out the message regardless if logging was not enabled nor configured
    print(Message)

    # Logging enabled, and custom filepath
    if LogEnable and LogLocation is not None:
        # Write to custom filepath
        WriteToLog(LogLocation, Message)

    # Logging was enabled, but likely no custom filepath
    elif LogEnable and LogLocation is None:
        # Create Log File with defaults
        CreateLogFile()
        WriteToLog(LogLocation, Message)

    # Logging is disabled and, and LogLocation is custom
    elif LogEnable is False and LogLocation is not None:
        print(f"LogLocation is configured to {LogLocation}, but logs are not enabled.\n"
              f"Enable Logging by running the function 'EnableLogging()' in your script.\n"
              f"Exiting script in 15 seconds...")
        time.sleep(15) # Can not use Wait() it will invoke PrintAndLog() again and loop
        exit()

    # Logging not enabled and no custom path set, default test behaviour
    else:
        return None

# Function to write to log
def WriteToLog(file, msg):
    # Logging enabled and custom filepath
    if LogEnable and LogLocation is not None:
        try: # write log to file
            with open(file, 'a') as file:
                file.write(CurrentTime() + " --- " + msg + "\n")
        except Exception as error:
            print(f"An error occurred writing to file: {error}")

    # Logging was enable but no custom filepath
    elif LogEnable and LogLocation is None:
        #Create Log File
        CreateLogFile()

        # Attempt to write log to file
        try:
            with open(file, 'a') as file:
                file.write(CurrentTime() + " --- " + msg + "\n")
        #
        except Exception as error:
            print(f"An error occurred writing to file: {error}")

    # Custom filepath for logging was set, but logging was NOT enabled
    else:
        print(f"LogLocation is configured to {LogLocation}, but logs are not enabled."
              f"Enable Logging by running the function 'EnableLogging()' in your script."
              f"Exiting script in 15 seconds...")
        Wait(15)
        exit()

# Handles errors that occur on website
def ErrorHandler(msg):

    # Print and log error
    PrintAndLog(f"\nError: \n{msg}")

    # Ask the user if they want to take a screenshot when error occurred
    i = input("\nDo you want to take a screenshot of the web page when error occurred? [y/n]")

    # if yes take a screenshot and log
    if i == "y" or i == "Y":
        PrintAndLog(f"Taking screenshot due to error: {msg}.")
        Screenshot(NamePrefix="Error")
        return None

    # If no, logs that no screenshot was saved
    else:
        PrintAndLog(f"Operator chose to not save screenshot of webpage when error occurred.")

    # Ask the operator if they want to attempt in continuing despite error
    j = input("\nDo you want to attempt to continue with existing error? [y/n]")

    # If yes, logs the error and the user wants to continue, returns None
    if j == "y" or j == "Y":
        PrintAndLog(f"User decided to continue after facing Error: {msg}.")
        return None

    # If no, logs termination due to error and quits
    else:
        PrintAndLog(f"User decided to terminate script after facing Error: {msg}.")
        CloseBrowser()

def ThrowIntentionalError(msg):
    PrintAndLog(f" Throwing Intentional Error: \n{msg}\n")

    # Ask the user if they want to continue
    answer = input("Do you want to continue? [y/n]")

    # If yes, logs the error and the user wants to continue, returns None
    if answer == "y" or answer == "Y":
        PrintAndLog(f"\nUser decided to continue after facing Error: {msg}.\n")
        return None
    # If no, logs termination due to error and quits
    else:
        PrintAndLog(f"\nUser decided to terminate script after facing Error: {msg}.\n")
        CloseBrowser()
        raise Exception(f"{msg}\n")
