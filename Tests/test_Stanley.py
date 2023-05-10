import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import pytest


class TestStanleyCaneca:

    @pytest.mark.stanley
    def test_canecona(self, driver):
        # go to webpage
        driver.get("https://eu.stanley1913.com/products/adventure-quencher-h2-0-flowstate-tumbler-40-oz")
        time.sleep(1)

        # check is sold out displayed
        sold_out_locator = driver.find_element(By.XPATH, "//*[@id='AddToCartText-7510939304136']")
        sold_out_txt = sold_out_locator.text
        assert sold_out_txt == "SOLD OUT", "OPS"