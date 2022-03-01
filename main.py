# Hack for https://monkeytype.com/

# Imports
import selenium
from selenium import webdriver
import pywinauto

# Set up webdriver
driver = webdriver.Chrome()

# Open monkeytye
driver.get('https://monkeytype.com/')


# Click on wordsWrapper
wordsWrapper = driver.find_element(by="id", value="wordsWrapper")
wordsWrapper.click()

# get all the words and make a sentence
words = driver.find_elements(by="class name", value="word")
sentence = ''
for word in words:
    # All letters are in <letter> tags
    letters = word.find_elements(by="tag name", value="letter")
    for letter in letters:
        sentence += letter.text
    sentence += ' '
print(sentence)

driver.close()


