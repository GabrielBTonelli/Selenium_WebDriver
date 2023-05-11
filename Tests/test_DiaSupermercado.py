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
        search_bar_locator = driver.find_element(By.ID, "search")
        search_bar_locator.send_keys("guinness")
        time.sleep(1)

        # pushing ENTER
        search_bar_locator.send_keys(Keys.ENTER)

        # verify new page URL contains "https://www.dia.es/compra-online/search?text=guinness&x=0&y=0"
        actual_url = driver.current_url
        assert actual_url == "https://www.dia.es/compra-online/search?text=guinness&x=0&y=0"
        
        # verify if product price is < than 2,99
        price_locator = driver.find_element(By.XPATH, "//*[@id='productgridcontainer']/div[1]/div/div/a/div[2]/div/p[1]")
        price_text = price_locator.text
        assert price_text != "2,99 €", "Price still " + price_text
