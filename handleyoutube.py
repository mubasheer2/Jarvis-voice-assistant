from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Inflow:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        
        # Initialize the Chrome service object
        service = Service(executable_path="/path/to/chromedriver")  # Replace with the correct path
        self.driver = webdriver.Chrome(options=options) 

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query="+query)
       
        # Use updated By.XPATH method
        
        
        enter = self.driver.find_element(By.XPATH, '//*[@id="dismissible"]/ytd-thumbnail')
        enter.click()

# Instantiate the class and search for 'hello'

