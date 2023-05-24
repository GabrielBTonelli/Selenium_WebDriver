from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BasePage:
    def openPage(self, driver):
        driver.get("https://eu.stanley1913.com/")
    
    def searchButton(self, driver):
        search_button = driver.find_element(By.XPATH, "//*[@id='shopify-section-header']/div[3]/div[3]/div/div/header/div[1]/div/div[3]/div/div/a[2]")
        driver.execute_script("arguments[0].click();", search_button)