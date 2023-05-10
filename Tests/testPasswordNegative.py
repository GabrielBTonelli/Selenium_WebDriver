import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class TestNegativePassword:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negativePassword(self):

# Open page
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")

# Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys( "student")

# Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password1234")

# Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

# Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should"


# Verify error message text is Your password is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"
