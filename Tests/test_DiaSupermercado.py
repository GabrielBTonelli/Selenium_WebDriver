import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import pytest

class TestPromoGuinnessDia:

    @pytest.mark.dia
    @pytest.mark.guinness
    def test_promoGuinness(self, driver):
        # go to webpage
        driver.get("https://www.dia.es/compra-online/")
        time.sleep(1)
        
        # Type "Guinness" on search bar
        search_bar_locator = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[1]/div[1]/div[2]/div/input")
        search_bar_locator.send_keys("guinness")
        time.sleep(1)

        # pushing ENTER
        search_bar_locator.send_keys(Keys.ENTER)
        
        # Guinness select
        # guinness = driver.find_element(By.XPATH, "//*[@id='searchComponent']/div/div[4]/div/ul/li/div/div[1]/div[2]/a[1]")
        # guinness.execute_script("arguments[0].click();", guinness)

        # verify if product price is < than 2,99
        price_locator = driver.find_element(By.XPATH, "//*[@id='searchComponent']/div/div[4]/div/ul/li/div/div[2]/div[1]/p[1]").text
        assert price_locator != "2,99 €", "Price still " + price_locator
