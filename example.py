# Created by dyeadal
# GNU General Public License 3.0

import seleniumlib as web

# Open Web Page
web.OpenPage("https://linkedin.com/in/diegoaalvarado")

# Wait for 1 - 10 seconds, randomly
web.RandomWait()

# Open Web Page
web.OpenPage("https://google.com")

# Store element as a variable to easily call on
SearchBar = web.FindElementByClass("gLFyf")

# Type some text into searchbar
web.TypeTextInClass(SearchBar,"Youtube")

# Press ENTER key on the search bar element
web.PressEnter(SearchBar)

# Store the first result element field as a varaible
FirstResults = web.FindElementByClass("IsZvec")

# Print out text contained in the first results element
web.TextInElement(FirstResults)

# Wait for exactly 10 seconds
web.Wait(100)

# Close the Web Browser
web.CloseBrowser()
