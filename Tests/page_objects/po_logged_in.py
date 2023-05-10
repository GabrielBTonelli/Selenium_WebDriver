from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support import expected_conditions as ec
from page_objects.po_base_page import BasePage

class LoggedIn(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __logOutButton_locator = (By.LINK_TEXT, "Log out")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)
    
    def logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logOutButton_locator)
    
    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, time=3)