from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

from utilities import ConfigReader


class AjaxPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clickon_AjaxBtn(self):
        """
        clicks on Dynamic ID Button
        """
        self.click("AjaxPage_TriggerBtn_Xpath")
        ajaxtext = WebDriverWait(self.driver, 15000).until(EC.visibility_of_element_located(
            (By.XPATH, ConfigReader.readconfig("locator", "AjaxPage_SuccessMsg_Xpath"))
        )).text
        print("value", ajaxtext)
