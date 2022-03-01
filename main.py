# Imports
import time
from selenium import webdriver
import pywinauto

class MonkeyTyper:
    def __init__(self) -> None:
        # Disable all notifications from selenium
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')

        # Set up webdriver
        self.driver = webdriver.Chrome(options=options)

        # Open monkeytye
        self.driver.get('https://monkeytype.com/')
        self._switch_to_words()

    # This is the function that switches to the words tab
    def _switch_to_words(self):
        """
        Switches to words tab
        Basically just clicks buttons and refreshes the page
        """
        f = self.driver.find_elements(by="class name", value='text-button')
        time.sleep(2)
        f[3].click()
        time.sleep(2)
        f = self.driver.find_elements(by="class name", value='text-button')
        for element in f:
            if element.get_attribute("wordcount") == "10":
                element.click()
                break
        # Reloads the page
        self.driver.refresh()

    # Gets the sentence using the page's HTML
    def _get_sentence(self):
        """
        Gets the sentence
        All sentences in monkeytype are in `word`
        In every word, there are <letter> tags
        
        This function collects everything into one sentence and returns it
        """
        time.sleep(2)
        # Clicks on wordsWrapper
        wordsWrapper = self.driver.find_element(by="id", value="wordsWrapper")
        try:
            wordsWrapper.click()
        except :
            pass
        # gets all the words and make a sentence
        words = self.driver.find_elements(by="class name", value="word")
        sentence = ''
        for word in words:
            # All letters are in <letter> tags
            letters = word.find_elements(by="tag name", value="letter")
            for letter in letters:
                if not "correct" in letter.get_attribute("class"):
                    # If the letter is not correct, adds it to the sentence
                    sentence += letter.text
            sentence += "{SPACE}"
        return sentence

    # Starts the typing
    def start(self):
        """
        Gets the sentence and starts typing
        """
        sentence = self._get_sentence()

        # TODO: Make this run faster somehow
        # Currently the typing speed is 199 💀 so annoying because it's so close to 200
        pywinauto.keyboard.send_keys(sentence+ "{TAB}{ENTER}")
        


if __name__ == '__main__':
    typer = MonkeyTyper()
    time.sleep(10) # Sleeping to allow the user to do stuff before starting
    i = 0
    while True:
        typer.start()
        i+=1