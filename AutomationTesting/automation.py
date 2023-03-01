'''
https://selenium-python.readthedocs.io/
http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/

utilize Selenium to automate moving around a webpage (i.e. without a human)
need to install via pip and include specific browser driver
typical install looks in PATH for driver file, otherwise specified

With selenium 4, get this warning:
DeprecationWarning: executable_path has been deprecated, please pass in a Service object chrome_browser = webdriver.Chrome('./chromedriver')
If you want it to go away (code will still work regardless), you can follow the instructions found here:
https://www.selenium.dev/documentation/getting_started/how_to_upgrade_to_selenium_4/#python-1

Sandbox for testing:
https://demo.seleniumeasy.com/

-easy to grab head elements, but not body
-there are several other options to grab elements (note... very different syntax in different selenium versions)
''' 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='./chromedriver')

chrome_browser = webdriver.Chrome(service=service)
chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

# add sleep if needed to keep window open. Selenium will automatically close the window otherwise.
# time.sleep(2)

# you can also use implicit vs explicit waits to act as a human
# chrome_browser.implicitly_wait(2)

# the $0 tag allows us to interact with an element
# for ex, get an attribute such as innerHTML
# this grabs whatever is within the brackets
show_message_button = chrome_browser.find_element(By.CLASS_NAME,'btn-default')
print(show_message_button)
print(show_message_button.get_attribute('innerHTML')) # should read 'Show Message'

# input message
# <input autofocus="" type="text" class="form-control" placeholder="Please enter your Message" id="user-message">
assert 'Show Message' in chrome_browser.page_source

user_string = 'I AM EXTRA COOOOL'
user_message = chrome_browser.find_element(By.ID,'user-message')
user_message.clear()
user_message.send_keys(user_string)

# simulate button click
# time.sleep(2)
show_message_button.click()

# output message
# <span id="display">asdf</span>
output_message = chrome_browser.find_element(By.ID,'display')
print(output_message)
print(user_string in output_message.text)
assert user_string in output_message.text

# you can also select by css selectors
user_button2 = chrome_browser.find_element(By.CSS_SELECTOR,'#get-input > .btn')
print(user_button2)

# if needed, close browsers
# chrome_browser.close()
# chrome_browser.quit()