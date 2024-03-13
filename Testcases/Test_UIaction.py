import time

from selenium.webdriver.common.by import By

from Pages.AjaxPage import AjaxPage
from Pages.DynamicIDPage import DynamicIdPage
from Pages.HomePage import HomePage
import pytest

from Pages.SampleAppPage import SampleAppPage
from Testcases.Test_Base import Test_BaseTest
import logging

from utilities import ConfigReader
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_uiaction(Test_BaseTest):

    def test_handledynamicid(self):
        """
        Test the Dynamic ID button
        """
        log.logger.info("Test  Handling Dynamic ID started")
        homepage = HomePage(self.driver)
        homepage.clickon_DynamicId()
        dynamicpage= DynamicIdPage(self.driver)
        dynamicpage.clickon_DynamicIdButton()
        homepage.navigateBackToHomePage()
        time.sleep(7)
        log.logger.info("Test Handling Dynamic ID ended")

    def test_verifysampleapp(self):
        """
        Test the Sample App login scenario
        """
        log.logger.info("Test Sample App started")
        homepage = HomePage(self.driver)
        homepage.clickon_SampleApp()
        samplepage = SampleAppPage(self.driver)
        samplepage.doLogin("anupriya", "pwd")
        elementText = self.driver.find_element(By.XPATH, ConfigReader.readconfig("locator",
                                                                                 "SampleAppPAge_Loginstatus_Xpath")).text

        assert elementText == "Welcome, anupriya!"
        time.sleep(6)
        log.logger.info("Test Sample App ended")

    def test_HandleAjax(self):
        """
        Handles Ajax Data
        """
        homepage = HomePage(self.driver)
        homepage.clickon_AjaxLink()
        ajaxpage= AjaxPage(self.driver)
        ajaxpage.clickon_AjaxBtn()
