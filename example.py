# Created by dyeadal
# GNU General Public License 3.0

import seleniumlib as web

# Open Web Page
web.OpenPage("https://linkedin.com/in/diegoaalvarado")

# Wait for 1 - 10 seconds, randomly
web.RandomWait()

# Open Web Page
web.OpenPage("https://google.com")

# Type some text in an element that can take keyboard input
web.TypeTextInClass("gLFyf","Youtube")

# Press ENTER key in an element
web.PressEnter("gLFyf")

# Wait for exactly 10 seconds
web.Wait(10)

# Close the Web Browser
web.CloseBrowser()
