import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import pytest

class TestOrderingSushi:

    def test_order_sushi(self, driver):

        # go to webpage
        driver.get("https://www.mikansushi.es/")

        # shows hidden login block
        icon_lock = driver.find_element(By.XPATH, "//*[@id='header']/div/div[1]/div[3]/div/div[2]/div/a/span/i")
        driver.execute_script("arguments[0].click();", icon_lock)
        time.sleep(1)

        # username and password insertion
        user_name_insert = driver.find_element(By.XPATH, "//*[@id='user_login']")
        user_name_insert.send_keys("")

        password_insert = driver.find_element(By.XPATH, "//*[@id='user_pass']")
        password_insert.send_keys("")

        # Click on loggin button
        loggin_button = driver.find_element(By.XPATH, "//*[@id='loginform']/div[3]/button")
        loggin_button.click()
        time.sleep(6)
