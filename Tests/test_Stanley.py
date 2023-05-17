import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import pytest


class TestStanleyCaneca:

    @pytest.mark.stanley
    # @pytest.mark.soldOut
    def test_quencher(self, driver):
        driver.get("https://eu.stanley1913.com/")
        # press search icon
        quencher_option = driver.find_element(By.XPATH, "//*[@id='shopify-section-header']/div[3]/div[3]/div/div/header/div[1]/div/div[2]/ul/li[2]/a")
        driver.execute_script("arguments[0].click();", quencher_option)
        time.sleep(3)
        # check quencher's availability 
        buy_bttn = driver.find_element(By.XPATH, "//*[@id='AddToCart-7510939304136']")
        assert buy_bttn.is_enabled(), "The Adventure Quencher 40 oz still Sold Out"
        
        

    @pytest.mark.stanley
    # @pytest.mark.soldOut
    def test_iceflow_89ml(self, driver):
        driver.get("https://eu.stanley1913.com/")

        # Search bttn click
        search_button = driver.find_element(By.XPATH, "//*[@id='shopify-section-header']/div[3]/div[3]/div/div/header/div[1]/div/div[3]/div/div/a[2]")
        driver.execute_script("arguments[0].click();", search_button)
        
        # seach for Stanley Classic Iceflow Flip
        search_input = driver.find_element(By.XPATH, "//*[@id='HeaderSearchForm']/input[2]")
        search_input.send_keys("Stanley Classic Iceflow Flip")
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)
        
        # IceFlow option click
        iceflow_option = driver.find_element(By.XPATH, "//*[@id='MainContent']/div/div/div/div/div[2]/div[2]/div[1]/a")
        driver.execute_script("arguments[0].click();", iceflow_option)
        time.sleep(1)
        
        # check Iceflow availability
        add_to_cart = driver.find_element(By.XPATH, "//*[@id='AddToCart-7520348700872']")
        assert add_to_cart.is_enabled(), "The Classic IceFlow 890mL still Sold Out"

        