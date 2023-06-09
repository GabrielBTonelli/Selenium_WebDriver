
import pytest
import time
from selenium.webdriver.common.by import By
# from page_objects.po_login_page import LoginPage


class TestNegativeScenarios:
    
    @pytest.mark.login
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser", "Password123", "Your username is invalid!"), ("student", "Password1234", "Your password is invalid!")])
    def test_negativeUsername(self, driver, username, password, expected_error_message):
        
        # login_page = LoginPage(driver)
        # login_page.open()
        # login_page.execute_login(username, password)
        # time.sleep(2)

        # assert login_page.get_error_message == expected_error_message, "Error message is not expected"

    
    
    # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

    # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

    # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)
    
    # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)
    
    # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should"

    
    # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"
    