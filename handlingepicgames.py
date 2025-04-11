from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Inflow:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
  
        self.driver = webdriver.Chrome( options=options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://store.epicgames.com/en-US/")
        
        # Wait for the search bar to be clickable and interact with it
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SearchLayout"]/div[1]/input')))
        search.click()
        search.send_keys(query)
        
        # Wait for the search button and click it
        enter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SearchLayout"]/div[1]/button')))
        enter.click()

# Instantiate the class and search for 'gta'
asseddrt = Inflow()
asseddrt.get_info("gta")
