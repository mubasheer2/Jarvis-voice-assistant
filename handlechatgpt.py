from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Inflow:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(options=options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://chatgpt.com/")
        
        # Wait until the prompt text area is loaded
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="prompt-textarea"]')))
        
        search.click()
        search.send_keys(query)
        
        # Attempt form submission with Enter key
        search.send_keys(Keys.RETURN)


