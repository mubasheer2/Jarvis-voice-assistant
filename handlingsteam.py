from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Inflow:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        
  
        self.driver = webdriver.Chrome(options=options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://store.steampowered.com/")
        
        # Wait for the search bar and interact with it
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="store_nav_search_term"]')))
        search.click()
        search.send_keys(query)
        
        # Wait for the search suggestions to load
        suggestions = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="search_suggestion_contents"]/a')))
        
        if suggestions:
            # Click on the first suggestion
            suggestions[0].click()
        else:
            print("No search suggestions found.")

# Instantiate the class and search for 'gta'
