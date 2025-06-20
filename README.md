# SeleniumLib  
A lightweight, human-like web automation helper built with undetected ChromeDriver and Python

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)

- [Features](https://github.com/dyeadal/seleniumlib/main/README.md#%EF%B8%8F-features)
- [Installation](https://github.com/dyeadal/seleniumlib/main/README.md#%EF%B8%8F-features)
  - [Windows](https://github.com/dyeadal/seleniumlib/main/README.md#%EF%B8%8F-features)
  - [Linux/MacOS](https://github.com/dyeadal/seleniumlib/main/README.md#%EF%B8%8F-features)  
- [Example Usage](https://github.com/dyeadal/seleniumlib/main/README.md#%EF%B8%8F-features)
- [Features in Development](https://github.com/dyeadal/seleniumlib/main/README.md#%EF%B8%8F-features)
- [Acknowledgements](https://github.com/dyeadal/seleniumlib/main/README.md#acknowledgements)
- [Disclaimer and Responsible Use](https://github.com/dyeadal/seleniumlib/main/README.md#%EF%B8%8F-disclaimer-and-responsible-use-%EF%B8%8F)

---

## ⚙️ Features

- **Undetected ChromeDriver** support to bypass bot detection  
- Human-like typing and random delays  
- Simulated scrolling and element interaction  
- Optional logging to file with timestamps  
- Screenshot capture with timestamped filenames  
- Simple element searching via class, ID, or any `By` selector (Selenium)
- Keyboard emulation (Enter, Page Down, etc.)

---

## Installation

### Windows 

Install selenium:
```python
pip install selenium
```

Install undetectable chromedriver by :
```python
pip install undetected-chromedriver
```

### Linux/MacOS
Install selenium:
```python
pip3 install selenium
```

Install undetectable chromedriver by :
```python
pip3 install undetected-chromedriver
```
---

## Example Usage

``` python
import seleniumlib as web

web.EnableLogging()                                         # Enable log output
web.CreateLogFile("/var/log/custom/", "customname")         # Initialize log file using specified directory and filename prefix
web.OpenPage("https://example.com")                         # Navigate to a URL
web.Wait(3)                                                 # Wait 3 seconds

element = web.FindElementByID("input")                      # Locate an element with an ID of "input" and store as a variable
web.TypeTextSlowly(element, "Hello")                        # Type slowly like a human
web.PressEnter(element)                                     # Press Enter on an element

web.Screenshot()                                            # Capture a screenshot
web.CloseBrowser()                                          # Exit browser

```

---

## Features in Development
- Ollama Thinking Models to generate text
- Ollama to store documents to guess prompted user responses

---

## Acknowledgements
This project uses the following open-source libraries:

- ### [Selenium](https://github.com/SeleniumHQ)

  Licensed under the Apache License 2.0.
  
  A browser automation framework and ecosystem. 

- ### [undetected-chromedriver(UCD)](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

  Licensed under the GPL-3.0 license.
  
  Custom Selenium Chromedriver | Zero-Config | Passes ALL bot mitigation systems (like Distil / Imperva/ Datadadome / CloudFlare IUAM)


Many thanks to the maintainers of these projects for making powerful tools freely available to the community.

---

## ⚠️ Disclaimer and Responsible Use ⚠️

This project is intended for educational and authorized automation only.

Do NOT use this tool to interact with websites without permission or in violation of their Terms of Service.

This script includes functionality that can mimic human interaction, which may bypass basic bot detection — use responsibly.

The author is not liable for any misuse or legal consequences resulting from unauthorized use.

Only test against systems you own or have explicit permission to automate.
