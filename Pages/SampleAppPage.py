from Pages.BasePage import BasePage


class SampleAppPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def doLogin(self, username, pswd):
        self.enterValue("SampleAppPage_UsernameTxt_Xpath", username)
        self.enterValue("SampleAppPage_PswdTxt_Xpath", pswd)
        self.click("SampleAppPage_LoginBtn_Xpath")
