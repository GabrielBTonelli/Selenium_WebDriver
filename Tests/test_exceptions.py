# https://practicetestautomation.com/practice-test-exceptions/

# import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.exceptions_page import ExceptionsPage

class TestExceptions:

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_no_such_ement_exceptions(self, driver):                    # Test 01
        
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 input should be displayed, but is not"
        
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # # Click Add button
        # click_add_button = driver.find_element(By.ID, "add_btn")
        # click_add_button.click()

        # wait = WebDriverWait(driver, timeout=10)
        # row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))    # Wait for the second row to load

        # # Verify Row 2 input field is displayed
        # assert row2_input_element.is_displayed(), "Row 2 input should be displayed, but is not."


    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):          # Test 02
        
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.add_second_food("Sushi")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message is not expected"

        
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # # Click Add button
        # click_add_button = driver.find_element(By.ID, "add_btn")
        # click_add_button.click()

        # # Wait for the second row to load
        # wait = WebDriverWait(driver, 10)
        # row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))    

        # # Type text into the second input field
        # row2_input_element.send_keys("Burrito")

        # # Push Save button using locator By.name(“Save”)
        # driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        # # Verify text saved
        # verify_text_saved = driver.find_element(By.ID, "confirmation")
        # verify_text_saved_txt = verify_text_saved.text
        # assert verify_text_saved_txt == "Row 2 was saved", "Confirmation message is not expected"


    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):         # Test 03
        
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        exceptions_page.add_second_food("sushi")
        assert exceptions_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message is not expected"

        
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # time.sleep(3)

        # # Clear input field
        # row1_edit_button = driver.find_element(By.ID, "edit_btn")
        # row1_edit_button.click()

        # row1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        # wait = WebDriverWait(driver, 10)
        # wait.until(ec.element_to_be_clickable(row1_input_element))
        # row1_input_element.clear()

        # # Type text into the input field
        # row1_input_element.send_keys("Sushi")
        # driver.find_element(By.XPATH, "//div[@id='row1']/button[@name='Save']").click()

        # # Verify text changed
        # confirmation_message = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        # conf_message = confirmation_message.text
        # assert conf_message == "Row 1 was saved", "Confirmation message is not expected"
        # # text = row1_input_element.get_attibute("value")
        # # assert text == "Sushi", "Expected Sushi but got" + text


    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):           # Test 04
        
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert not exceptions_page.are_instructions_displayed(), "Instruction text element should not be displayed"
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # time.sleep(2)
        
        # # Push add button
        # click_add_button = driver.find_element(By.ID, "add_btn")
        # click_add_button.click()
        
        # # Verify instruction text element is no longer displayed
        # wait = WebDriverWait(driver, 10)
        # assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions"))), "Instruction text element should no be displayed"


    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_time_out_exception(self, driver):                          # Test 05
        
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.add_second_row()
        assert exceptions_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"
        
        
        # # Open page
        # driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # time.sleep(2)

        # # Click Add button
        # click_add_button = driver.find_element(By.ID, "add_btn")
        # click_add_button.click()

        # # Wait for 3 seconds for the second input field to be displayed
        # wait = WebDriverWait(driver, 6)
        # row2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # # Verify second input field is displayed
        # assert row2_input_element.is_displayed(), "Row 2 input field should be displayed but is not"