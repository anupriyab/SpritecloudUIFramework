import time

from Pages.HomePage import HomePage
import pytest

from Pages.SampleAppPage import SampleAppPage
from Testcases.Test_Base import Test_BaseTest
import logging
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_UIaction(Test_BaseTest):

    def test_verifyId(self):
        log.logger.info("Test Sign up started")
        print("verifying the dynamic id")
        homepage = HomePage(self.driver)
        homepage.clickon_DynamicId()
        time.sleep(6)
        log.logger.info("Test Sign up ended")

    def test_verifySampleApp(self):
        log.logger.info("Test Sign up started")
        print("verifying the sample app")
        homepage = HomePage(self.driver)
        homepage.clickon_SampleApp()
        samplepage = SampleAppPage(self.driver)
        samplepage.doLogin("anupriya", "pwd")
        time.sleep(6)
        log.logger.info("Test Sign up ended")
