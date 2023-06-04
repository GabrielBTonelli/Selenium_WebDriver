import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_objects import po_Stanley
import pytest

class TestStanleyCaneca:

    @pytest.mark.stanley
    # @pytest.mark.soldOut
    def test_quencher(self, driver):
        po_Stanley.BasePage.openPage(self, driver)
        # press quencher icon
        quencher_option = driver.find_element(By.XPATH, "//*[@id='shopify-section-header']/div[3]/div[3]/div/div/header/div[1]/div/div[2]/ul/li[2]/a")
        driver.execute_script("arguments[0].click();", quencher_option)
        time.sleep(3)
        # check quencher's availability 
        buy_bttn = driver.find_element(By.XPATH, "//*[@id='AddToCart-7510939304136']")
        assert buy_bttn.is_enabled(), "The Adventure Quencher 40 oz still Sold Out"
        
        

    @pytest.mark.stanley
    # @pytest.mark.soldOut
    def test_iceflow_89ml(self, driver):
        po_Stanley.BasePage.openPage(self, driver)
        po_Stanley.BasePage.productLocalizer(self, driver)
         
        # seach for Stanley Classic Iceflow Flip
        search_input = driver.find_element(By.XPATH, "//*[@id='HeaderSearchForm']/input[2]")
        search_input.send_keys("Stanley Classic Iceflow Flip")
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)
        
        # IceFlow option click
        iceflow_option = driver.find_element(By.XPATH, "//*[@id='MainContent']/div/div/div/div/div[2]/div[1]/div[1]/a/div[1]/div[7]")
        driver.execute_script("arguments[0].click();", iceflow_option)
        time.sleep(1)
        
        # check Iceflow availability
        add_to_cart = driver.find_element(By.XPATH, "//*[@id='AddToCartText-7520348700872']").text
        assert add_to_cart == "ADD TO CART", "The Classic IceFlow 890mL still Sold Out"

    @pytest.mark.stanley
    # @pytest.mark.soldOut
    def test_goFlip_650mL(self, driver):
        po_Stanley.BasePage.openPage(self, driver)
        po_Stanley.BasePage.productLocalizer(self, driver)
        
        # seach for Stanley Go Flip
        search_input = driver.find_element(By.XPATH, "//*[@id='HeaderSearchForm']/input[2]")
        search_input.send_keys("STANLEY GO FLIP STRAW WATER BOTTLE | 0.65L")
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)
        
        # GoFlip option click
        goFlip_option = driver.find_element(By.XPATH, "//*[@id='MainContent']/div/div/div/div/div[2]/div[1]/div[1]/a")
        driver.execute_script("arguments[0].click();", goFlip_option)
        time.sleep(1)
        
        # check Iceflow availability
        add_to_cart = driver.find_element(By.XPATH, "//*[@id='AddToCartText-6256539467976']")
        assert add_to_cart.is_enabled(), "The Stanley Go Flip Straw 650mL still Sold Out"
